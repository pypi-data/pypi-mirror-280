import os
import json
from typing import List, Optional
from enum import Enum

from betteryeah.generic_client import GenericPlugin
from betteryeah.marketing_client import XiaoHongShuPlugin, ZhihuPlugin, WeiboPlugin, DouyinPlugin, \
    ToutiaoPlugin, BilibiliPlugin
from betteryeah.parse_client import WebParsingClient, ExcelParsingClient, AudioParsingClient, ArticleParsingClient, \
    ArticleParsingModel, VideoParsingClient, AnalysisModeType, OCRFlowClient
from betteryeah.response import LLMResponse, SearchKnowledgeResponse, ExecuteDatabaseResponse, InsertKnowledgeResponse, \
    GenerateImageResponse, VisionImageResponse, SearchResponse, SubFlowResponse, WebParsingResponse, \
    ExcelParsingResponse, AudioParsingResponse, VideoParsingResponse, ExcelOutputType, LLMAvailableModelResponse
from betteryeah.utils import type_check, send_request


class Model(Enum):
    gpt_3_5_turbo = "gpt-3.5-turbo"
    gpt_3_5_turbo_16k = "gpt-3.5-turbo-16k"
    gpt_4_turbo = "gpt-4-turbo"
    gpt_4o = "gpt-4o"
    chatglm_lite = "chatglm_lite"
    chatglm_lite_32k = "chatglm_lite_32k"
    chatglm_pro = "chatglm_pro"
    chatglm_std = "chatglm_std"
    qwen_turbo = "qwen-turbo"
    qwen_plus = "qwen-plus"
    ERNIE_Bot = "ERNIE-Bot"
    ERNIE_Bot_turbo = "ERNIE-Bot-turbo"
    ERNIE_Bot_4 = "ERNIE-Bot-4"
    Qianfan_Chinese_Llama_2_7B = "Qianfan_Chinese_Llama_2_7B"
    ChatGLM2_6B_32K = "ChatGLM2_6B_32K"
    Llama_2_7b_chat = "Llama-2-7b-chat"
    AquilaChat_7B = "AquilaChat_7B"
    BLOOMZ_7B = "BLOOMZ-7B"
    Llama_2_70b_chat = "Llama-2-70b-chat"
    anthropic_claude_v2 = "anthropic.claude-v2"
    anthropic_claude_instant_v1 = "anthropic.claude-instant-v1"
    anthropic_claude_3_sonnet = "anthropic.claude-3-sonnet"
    anthropic_claude_3_opus = "anthropic.claude-3-opus"
    generalv2 = "generalv2"
    general = "general"
    HuanYuan = "HuanYuan"
    GLM_3_Turbo = "GLM-3-Turbo"
    GLM_4V = "GLM-4V"
    GLM_4 = "GLM-4"
    glm_4_9b = "glm-4-9b"
    gemini = "gemini"
    anthropic_claude_3_haiku = "anthropic.claude-3-haiku"
    gemini_1_5_pro = "Gemini 1.5 Pro"
    moonshot_v1_8k = "moonshot-v1-8k"
    moonshot_v1_32k = "moonshot-v1-32k"
    moonshot_v1_128k = "moonshot-v1-128k"
    skylark2_pro_32k = "skylark2-pro-32k"
    skylark2_pro_turbo_8k = "skylark2-pro-turbo-8k"
    BTY_NeuroText_Enhanced = "BTY-NeuroText-Enhanced"
    claude_3_opus = "claude-3-opus"
    deepseek_chat = "deepseek-chat"
    doubao_pro_128 = "Doubao-pro-128k"
    doubao_pro_32 = "Doubao-pro-32k"
    doubao_pro_4 = "Doubao-pro-4k"


class GenerateImageModel(Enum):
    gpt_4o = "gpt-4o"
    gpt_4_vision_preview = "gpt-4-vision-preview"
    anthropic_claude_3_sonnet = "anthropic.claude-3-sonnet"
    anthropic_claude_3_haiku = "anthropic.claude-3-haiku"
    gemini_1_5_Pro = "Gemini 1.5 Pro"
    gemini_1_5_Flash = "Gemini 1.5 Flash"
    gemini_1_0_Pro_Vision = "Gemini 1.0 Pro Vision"


class MemoryType(Enum):
    INSERT_MEMORY = "insertMemory"
    SEARCH_MEMORY = "searchMemory"


class OutPutType(Enum):
    TEXT = "text"
    JSON = "json"


class HitStrategyType(Enum):
    MIX = 1
    KEY = 2
    SEMANTICS = 3


class SubPluginImage:
    async def vision(self, image_path: List[str], prompt: str = None,
                     model: GenerateImageModel = GenerateImageModel.gpt_4o) -> VisionImageResponse:
        r"""
        AI识图
        :param image_path: 图像的链接地址
        :param prompt: 图像的提示词
        :param model: AI识图使用的模型
        """
        return await VisionImageClient().recognition(image_path=image_path, prompt=prompt, model=model)

    async def generate(self, prompt) -> GenerateImageResponse:
        r"""
        AI生图,如果成功,返回GenerateImageResponse实例的一个对象,这个对象的data属性中包含一个message对象.该对象
        存储生成的图片的url地址
        :param prompt: 图像的提示词
        :return:GenerateImageResponse的一个对象
        """
        return await GenerateImageClient().generate(prompt=prompt)

    async def ocr(self, image_url: str):
        r"""
        使用ocr进行图片识别
        :param image_url: 要识别的图片的url地址数组
        """
        return await OCRFlowClient().parse(image_url)


class SubPluginSearch:
    async def google(self, question: str, parse_web_count: int = 2, domain_name: str = None) -> SearchResponse:
        r"""
        搜索google并返回信息
        :param question: 要搜索的内容
        :param parse_web_count: 解析链接数量,默认为2
        :param domain_name: 指定域名搜索
        :return:SearchResponse的一个对象
        """
        return await GoogleSearchClient().search(question=question, parse_web_count=parse_web_count,
                                                 domain_name=domain_name)

    async def bing(self, question: str, parse_web_count: int = 2, domain_name: str = None) -> SearchResponse:
        r"""
        搜索bing并返回信息
        :param question: 要搜索的内容
        :param parse_web_count: 解析链接数量,默认为2
        :param domain_name: 指定域名搜索
        :return:SearchResponse的一个对象
        """
        return await BingSearchClient().search(question=question, parse_web_count=parse_web_count,
                                               domain_name=domain_name)


class SubPluginParsing:
    async def web(self, url_list: List[str]) -> WebParsingResponse:
        r"""
        :param url_list: 要解析的url地址
        """
        return await WebParsingClient().parse(url_list=url_list)

    async def excel(self, excel_url: str,
                    output_format: ExcelOutputType = ExcelOutputType.HTML) -> ExcelParsingResponse:
        r"""
        :param excel_url: 要解析的excel url地址
        :param output_format: 输出格式
        """
        return await ExcelParsingClient().parse(excel_url=excel_url, output_format=output_format)

    async def audio(self, audio_url: str, auto_split: bool = True) -> AudioParsingResponse:
        r"""
        :param audio_url: 要解析的音频 url地址
        :param auto_split: 是否进行智能分轨,默认为True
        """
        return await AudioParsingClient().parse(audio_url=audio_url, auto_split=auto_split)

    async def video(self, video_url: str,
                    analysis_mode: AnalysisModeType = AnalysisModeType.ScreenshotAndAudio) -> VideoParsingResponse:
        r"""
        解析视频文件,如果AnalysisModeType为OnlyAudio,返回值的data中为字符串,
        如果AnalysisModeType为ScreenshotAndAudio,则返回值data中为List[VideoParsingItem]
        对象
        :param video_url: 解析的视频
        :param analysis_mode: 解析的模式
        """
        return await VideoParsingClient().parse(video_url, analysis_mode)

    async def article(self, long_text_list: List[str], analysis_description: str = "请解析",
                      model: ArticleParsingModel = ArticleParsingModel.Claude) -> AudioParsingResponse:
        r"""
        解析长文本插件
        :param long_text_list: 长文本的文件url地址,该数组的长度最大为2
        :param analysis_description: 解析要求
        :param model: 选择的模型类型
        """
        return await ArticleParsingClient().parse(long_text_list=long_text_list,
                                                  analysis_description=analysis_description,
                                                  model_type=model)


class Plugin:
    image = SubPluginImage()
    search = SubPluginSearch()
    parsing = SubPluginParsing()
    generic = GenericPlugin()
    xiaohongshu = XiaoHongShuPlugin()
    zhihu = ZhihuPlugin()
    weibo = WeiboPlugin()
    douyin = DouyinPlugin()
    toutiao = ToutiaoPlugin()
    bilibili = BilibiliPlugin()


# 客户端基类
class BetterYeah:
    def __init__(self, api_key: str = None, workspace_id: str = None, flow_id: str = "-1", app_id: str = "-1"):
        self.llm = LLMClient()
        self.database = DatabaseClient()
        self.knowledge = KnowledgeClient()
        self.plugin = Plugin()
        self.sub_flow = SubFlowClient()
        if api_key is not None:
            os.environ['API_KEY'] = api_key

        self._config = {}
        if workspace_id is not None:
            self._config["workspace_id"] = workspace_id
        if flow_id is not None:
            self._config["flow_id"] = flow_id
        if flow_id is not None:
            self._config["app_id"] = app_id
        if os.environ.get('RUN_ARGS') is None:
            os.environ['RUN_ARGS'] = json.dumps(self._config)


# 聊天客户端
class LLMClient:

    async def chat(self, system_prompt: str, model: Model | str = Model.gpt_3_5_turbo, json_mode: bool = False,
                   messages: Optional[List[dict]] = None, temperature: float = 0.7) -> LLMResponse:
        r"""
        :param system_prompt: 用户输入的prompt
        :param model: 选择的对应模型
        :param json_mode: 输出的文本类型是否是json格式,注意,若为True,请在system_prompt中明确声明返回json的key
        的形式,否则模型会随机返回json的key
        :param messages: 上下文历史信息,例如:[{"role": "user","content": "你好"},{"role": "assistant","content": "你好，有什么可以帮助您？"}]
        :param temperature: 模型对应的temperature参数
        :return:例如:{'code': 200, 'success': True, 'message': 'SUCCESS', 'data': '汉朝一共有26位皇帝。', 'now_time': 1715395402}
        """
        # 处理 model 参数
        data = {
            "name": "LLM",
            "parameters": {
                "inputs": {
                    "model": model if isinstance(model, str) else model.value,
                    "plugin": {"json_mode": json_mode},
                    "stream": False,
                    "messages": [] if messages is None else messages,
                    "temperature": temperature,
                    "context_type": "messageList",
                    "system_prompt": system_prompt,
                }
            }
        }
        return LLMResponse(await send_request("POST", data))

    async def get_available_models(self) -> LLMAvailableModelResponse:
        r"""
        获取当前可用的模型列表
        :return:
        """
        return LLMAvailableModelResponse(await send_request("GET", data={}, endpoint="/active_channels"))


# 数据库客户端
class DatabaseClient:

    @type_check
    async def execute_database(self, base_id: str, executable_sql: str) -> ExecuteDatabaseResponse:
        r"""
        操作数据库
        :param base_id:数据库的id
        :param executable_sql:执行数据库的对应的sql
        """
        data = {
            "name": "DATABASE",
            "parameters": {
                "inputs": {
                    "baseId": base_id,
                    "executableSQL": executable_sql
                }
            }
        }
        return ExecuteDatabaseResponse(await send_request("POST", data))


# 知识库客户端
class KnowledgeClient:

    @type_check
    async def insert_knowledge(self, content: str, file_id: int, partition_id: int = None) -> InsertKnowledgeResponse:
        r"""
        插入知识库
        :param content: 要插入的知识库的内容
        :param file_id: 插入的知识库id
        :param partition_id: 知识库对应的partition_id
        """
        data = {
            "name": "KNOWLEDGE",
            "parameters": {
                "inputs": {
                    "content": content,
                    "file_id": file_id,
                    "memoryType": MemoryType.INSERT_MEMORY.value,
                    "partition_id": partition_id,
                },
            }
        }
        return InsertKnowledgeResponse(await send_request("POST", data))

    @type_check
    async def search_knowledge(self, search_content: str, partition_id: int, file_ids: Optional[List[int]] = None,
                               tags: Optional[List[str]] = None,
                               output_type: OutPutType = OutPutType.TEXT,
                               hit_strategy: HitStrategyType = HitStrategyType.MIX,
                               max_result_num: int = 3, ranking_strategy: bool = False) -> SearchKnowledgeResponse:
        r"""
        查询知识库
        :param search_content: 查询的内容信息
        :param partition_id: 文件的 partition_id
        :param file_ids: 文件的id列表
        :param tags: 标签名称
        :param output_type: 选择输出类型
        :param hit_strategy: OutPutType中的对象,MIX表示混合查询，KEY表示关键字查询，SEMANTICS表示语义查询
        :param max_result_num: 最大结果数 1-10
        :param ranking_strategy: 指令重排，默认是0,支持指令重排是1
        """
        data = {
            "name": "KNOWLEDGE",
            "parameters": {
                "inputs": {
                    "tags": tags,
                    "memory": partition_id,
                    "file_ids": file_ids,
                    "memoryType": MemoryType.SEARCH_MEMORY.value,
                    "outputType": output_type.value,
                    "hitStrategy": hit_strategy.value,
                    "maxResultNum": max_result_num,
                    "searchContent": search_content,
                    "rankingStrategy": 1 if ranking_strategy else 0
                }
            }
        }
        return SearchKnowledgeResponse(await send_request("POST", data))


class VisionImageClient:

    async def recognition(self, image_path: List[str], prompt: str = None,
                          model: GenerateImageModel = GenerateImageModel.gpt_4o) -> VisionImageResponse:
        r"""
        AI识图
        :param image_path: 图像的链接地址
        :param prompt: 图像的提示词
        :param model: AI识图使用的模型
        """
        if not isinstance(image_path, str):
            tmp_images = []
            [tmp_images.append({"value": i}) for i in image_path]
            image_path = tmp_images
        data = {
            "name": "VISION_IMAGE",
            "parameters": {
                "inputs": {
                    "question": prompt,
                    "image_path": image_path,
                    "model": model.value
                }
            }
        }
        return VisionImageResponse(await send_request("POST", data))


class GenerateImageClient:

    async def generate(self, prompt: str = None) -> GenerateImageResponse:
        r"""
        AI生图,如果成功,返回GenerateImageResponse实例的一个对象,这个对象的data属性中包含一个message对象.该对象
        存储生成的图片的url地址
        :param prompt: 图像的提示词
        :return:GenerateImageResponse的一个对象
        """
        data = {
            "name": "GENERATE_IMAGE",
            "parameters": {
                "inputs": {
                    "prompt": prompt,
                }
            }
        }
        return GenerateImageResponse(await send_request("POST", data))


class GoogleSearchClient:

    async def search(self, question: str, parse_web_count: int = 2, domain_name: str = None) -> SearchResponse:
        r"""
        搜索google并返回信息
        :param question: 要搜索的内容
        :param parse_web_count: 解析链接数量,默认为2
        :param domain_name: 指定域名搜索
        :return:SearchResponse的一个对象
        """
        data = {
            "name": "GOOGLE_SEARCH",
            "parameters": {
                "inputs": {
                    "question": question,
                    "parse_web_count": parse_web_count,
                    "domain_name": domain_name
                }
            }
        }
        return SearchResponse(await send_request("POST", data))


class BingSearchClient:
    async def search(self, question: str, parse_web_count: int = 2, domain_name: str = None) -> SearchResponse:
        r"""
        搜索bing并返回信息
        :param question: 要搜索的内容
        :param parse_web_count: 解析链接数量,默认为2
        :param domain_name: 指定域名搜索
        :return:SearchResponse的一个对象
        """
        data = {
            "name": "BING_SEARCH",
            "parameters": {
                "inputs": {
                    "question": question,
                    "parse_web_count": parse_web_count,
                    "domain_name": domain_name
                }
            }
        }
        return SearchResponse(await send_request("POST", data))


class SubFlowClient:

    async def execute(self, flow_id: str, parameter: dict = None) -> SubFlowResponse:
        r"""
        执行子flow并返回子flow的结果
        :param flow_id: 要执行子flow的id
        :param parameter: 执行的参数
        """
        if parameter is None:
            parameter = {}
        data = {
            "name": "SUB_FLOW",
            "parameters": {
                "inputs": parameter,
                "flow_id": flow_id
            }
        }
        return SubFlowResponse(await send_request("POST", data))
