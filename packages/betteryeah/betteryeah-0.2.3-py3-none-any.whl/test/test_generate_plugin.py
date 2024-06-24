import asyncio
import json
import os

from betteryeah import BetterYeah, Model, GenerateImageModel, ArticleParsingModel, \
    AnalysisModeType, OutPutType, HitStrategyType
from betteryeah import ExcelOutputType

# http://localhost:8001
# https://dev-ai-api.betteryeah.com
os.environ['GEMINI_SERVER_HOST'] = 'https://dev-ai-api.betteryeah.com'
abc = BetterYeah(api_key="NjVhZTA5YTBlMWMzMDIyNGM5MThjMGE5LDIwMzIsMTcxNDM3MTMyODQ1NQ==")


"工作流"
result = asyncio.run(
    abc.sub_flow.execute(
        flow_id="bacdb3af1de6464ab4d277a16903f93d",
        parameter={"message": "你好"}
    ))
print(result)

result = asyncio.run(abc.llm.chat(
    '中国的汉朝有几位皇帝',
    json_mode=False,
    model=Model.doubao_pro_128,
    messages=[],
    temperature=0.0
))
print(result)

datas = {
    "Apple": 98,
    "XiaoMi": 90,
    "HuaWei": 92,
    "Oppo": 88
}

result = asyncio.run(abc.plugin.generic.chart_plotting(requirements="按照各个手机品牌的受欢迎统计数据绘制一个柱形图",
                                                       data_desc="各个手机品牌受欢迎程度统计结果数据",
                                                       data=json.dumps(datas)))
print(result)
result = asyncio.run(abc.plugin.generic.chart_plotting(requirements="按照各个手机品牌的受欢迎统计数据绘制一个柱形图",
                                                       data_desc="各个手机品牌受欢迎程度统计结果数据",
                                                       excel_file="https://resource.bantouyan.com/betteryeah/temp/data_example.xlsx"))
print(result)

"KNOWLEDGE"
"插入"
result = asyncio.run(abc.knowledge.insert_knowledge("测试", partition_id=375, file_id=1654))
print(result)
"查询"
result = asyncio.run(abc.knowledge.search_knowledge(
    search_content="测试",
    partition_id=375,
    tags=[],
    file_ids=[1654],
    output_type=OutPutType.JSON,
    hit_strategy=HitStrategyType.MIX,
    max_result_num=3,
    ranking_strategy=False
))
print(result)


"database"
result = asyncio.run(abc.database.execute_database(
    base_id="p87z22yaps8fcas",
    executable_sql="select * from test limit 100"
))
print(result)


"LLM"
result = asyncio.run(abc.llm.chat(
    '中国的汉朝有几位皇帝',
    json_mode=False,
    model=Model.gpt_3_5_turbo,
    messages=[],
    temperature=0.0
))
print(result)

"图像处理"
"生图"
result = asyncio.run(abc.plugin.image.generate("帮我生成一张宝塔的图片"))
print(result)
"识图"
result = asyncio.run(abc.plugin.image.vision(
    image_path="https://resource.bantouyan.com/betteryeah/temp/FIlP_1716862566510.jpg",  # 图片地址
    prompt="图片中的物体是什么",
    model=GenerateImageModel.gpt_4o
))
print(result)
"OCR"
result = asyncio.run(abc.plugin.image.ocr("https://resource.bantouyan.com/betteryeah/temp/example.png"))
print(result)

"网络搜索"
"google"
result = asyncio.run(abc.plugin.search.google(question="汉朝皇帝列表"))
print(result)
"bing"
result = asyncio.run(abc.plugin.search.bing("汉朝皇帝列表"))
print(result)

"解析能力"
"excel(未完成)"
result = asyncio.run(abc.plugin.parsing.excel("https://resource.bantouyan.com/betteryeah/temp/example.xlsx",
                                              output_format=ExcelOutputType.JSON))
print(result)
"网页"
result = asyncio.run(abc.plugin.parsing.web(["https://www.betteryeah.com", "https://www.betteryeah.com/solution"]))
print(result)
"长文本"
result = asyncio.run(abc.plugin.parsing.article([
    "https://resource.bantouyan.com/betteryeah/temp/example.txt",
], analysis_description="请根据url进行解析", model=ArticleParsingModel.Claude))
print(result)
"音频"
result = asyncio.run(abc.plugin.parsing.audio(
    "https://resource.bantouyan.com/betteryeah/temp/example.wav",
    False
))
print(result)
"视频"
result = asyncio.run(
    abc.plugin.parsing.video("https://dev-ai-api.betteryeah.com/v1/chat/file/38d41aa512a5417d890bac8adf262b43",
                             AnalysisModeType.OnlyAudio))
print(result)

"工作流"
result = asyncio.run(
    abc.sub_flow.execute(
        flow_id="a50739fc30534178a8a8028ca660fdad",
        parameter={"message": "你好"}
    ))
print(result)
