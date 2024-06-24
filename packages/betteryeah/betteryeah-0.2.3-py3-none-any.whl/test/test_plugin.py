import asyncio

from betteryeah import ExcelOutputType
from betteryeah import GenerateImageModel, ArticleParsingModel, \
    AnalysisModeType
from test_base import better_yeah

"图像处理"
"生图"
result = asyncio.run(better_yeah.plugin.image.generate("帮我生成一张宝塔的图片"))
print(result)
"识图"
result = asyncio.run(better_yeah.plugin.image.vision(
    image_path="https://resource.bantouyan.com/betteryeah/temp/FIlP_1716862566510.jpg",  # 图片地址
    prompt="图片中的物体是什么",
    model=GenerateImageModel.gpt_4o
))
print(result)
"OCR"
result = asyncio.run(better_yeah.plugin.image.ocr("https://resource.bantouyan.com/betteryeah/temp/example.png"))
print(result)

"网络搜索"
"google"
result = asyncio.run(better_yeah.plugin.search.google(question="汉朝皇帝列表"))
print(result)
"bing"
result = asyncio.run(better_yeah.plugin.search.bing("汉朝皇帝列表"))
print(result)

"解析能力"
"excel(未完成)"
result = asyncio.run(better_yeah.plugin.parsing.excel("https://resource.bantouyan.com/betteryeah/temp/example.xlsx",
                                              output_format=ExcelOutputType.JSON))
print(result)
"网页"
result = asyncio.run(better_yeah.plugin.parsing.web(["https://www.betteryeah.com", "https://www.betteryeah.com/solution"]))
print(result)
"长文本"
result = asyncio.run(better_yeah.plugin.parsing.article([
    "https://resource.bantouyan.com/betteryeah/temp/example.txt",
], analysis_description="请根据url进行解析", model=ArticleParsingModel.Claude))
print(result)
"音频"
result = asyncio.run(better_yeah.plugin.parsing.audio(
    "https://resource.bantouyan.com/betteryeah/temp/example.wav",
    False
))
print(result)
"视频"
result = asyncio.run(
    better_yeah.plugin.parsing.video("https://resource.bantouyan.com/betteryeah/temp/example.mp4",
                             AnalysisModeType.OnlyAudio))
print(result)

"工作流"
result = asyncio.run(
    better_yeah.sub_flow.execute(
        flow_id="a50739fc30534178a8a8028ca660fdad",
        parameter={"message": "你好"}
    ))
print(result)
