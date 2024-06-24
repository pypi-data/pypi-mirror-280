from enum import Enum
from typing import List

from betteryeah.response import WebParsingResponse, ExcelParsingResponse, AudioParsingResponse, VideoParsingResponse, \
    OCRParsingResponse, ExcelOutputType
from betteryeah.utils import type_check, send_request


class WebParsingClient:

    async def parse(self, url_list: List[str]) -> WebParsingResponse:
        r"""
        :param url_list: 要解析的url地址数组
        """
        if len(url_list) < 1:
            return WebParsingResponse({'code': 200, 'success': True, 'message': 'SUCCESS', 'data': []})
        # 处理 model 参数
        data = {
            "name": "WEB_PARSING",
            "parameters": {
                "inputs": {
                    "url": ",".join(url_list),
                }
            }
        }
        return WebParsingResponse(await send_request("POST", data))


class ExcelParsingClient:

    @type_check
    async def parse(self, excel_url: str,
                    output_format: ExcelOutputType = ExcelOutputType.JSON) -> ExcelParsingResponse:
        r"""
        :param excel_url: 要解析的excel url地址
        :param output_format: 输出格式
        """
        # 处理 model 参数
        data = {
            "name": "EXCEL_PARSING",
            "parameters": {
                "inputs": {
                    "excel_url": excel_url,
                    "output_format": output_format.value
                }
            }
        }
        return ExcelParsingResponse(await send_request("POST", data))


class AudioParsingClient:

    @type_check
    async def parse(self, audio_url: str, auto_split: bool = True) -> AudioParsingResponse:
        r"""
        :param audio_url: 要解析的音频 url地址
        :param auto_split: 是否进行智能分轨,默认为True
        """
        # 处理 model 参数
        data = {
            "name": "AUDIO_PARSING",
            "parameters": {
                "inputs": {
                    "audio_url": audio_url,
                    "auto_split": auto_split
                }
            }
        }
        return AudioParsingResponse(await send_request("POST", data))


class ArticleParsingModel(Enum):
    Kimi = "Kimi"
    Claude = "Claude"


class ArticleParsingClient:

    async def parse(self, long_text_list: List[str], analysis_description: str = "请解析",
                    model_type: ArticleParsingModel = ArticleParsingModel.Claude) -> AudioParsingResponse:
        r"""
        :param long_text_list: 长文本的文件url地址,该数组的长度最大为2
        :param analysis_description: 解析要求
        :param model_type: 选择的模型类型
        """
        data = {
            "name": "ARTICLE_PARSING",
            "parameters": {
                "inputs": {
                    "long_text_list": [{"value": item} for item in long_text_list],
                    "analysis_description": analysis_description,
                    "model_type": model_type.value
                }
            }
        }
        return AudioParsingResponse(await send_request("POST", data))


class AnalysisModeType(Enum):
    ScreenshotAndAudio = 0
    OnlyAudio = 1


class VideoParsingClient:
    async def parse(self, video_url: str,
                    analysis_mode: AnalysisModeType = AnalysisModeType.ScreenshotAndAudio) -> VideoParsingResponse:
        r"""
        :param analysis_mode: 长文本的文件url地址,该数组的长度最大为2
        :param video_url: 解析要求
        :param analysis_mode: 选择的模型类型
        """
        data = {
            "name": "VIDEO_PARSING",
            "parameters": {
                "inputs": {
                    "video_url": video_url,
                    "analysis_mode": analysis_mode.value
                }
            }
        }
        return VideoParsingResponse(await send_request("POST", data))


class OCRFlowClient:
    async def parse(self, image_url: str) -> OCRParsingResponse:
        r"""
        OCR识图
        :param image_url: 要解析的ocr url地址数组
        """
        data = {
            "name": "OCR_PARSING",
            "parameters": {
                "inputs": {
                    "image_url": image_url
                }
            }
        }
        return OCRParsingResponse(await send_request("POST", data))
