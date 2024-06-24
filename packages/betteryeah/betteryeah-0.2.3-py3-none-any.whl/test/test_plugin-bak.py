import asyncio
import os
from typing import Optional

from betteryeah import BetterYeah, OutPutType, HitStrategyType, Model

# http://localhost:8001
# https://dev-ai-api.betteryeah.com
os.environ['GEMINI_SERVER_HOST'] = 'http://localhost:8001'
abc = BetterYeah(api_key="NjVhZTA5YTBlMWMzMDIyNGM5MThjMGE5LDIwMzIsMTcxNDM3MTMyODQ1NQ==")
'''
os.environ[
    'RUN_ARGS'] = ('{"flow_id": "f8c252e9c3794c13a523147ee1c5cb89", "workspace_id": "65ae09a0e1c30224c918c0a9", "app_id": "f8c252e9c3794c13a523147ee1c5cb89",'
                   ' "user_id": 2032, "user_name": "18757159087", "enterprise_id": null, "task_id": "2cc43450-8cdc-45da-b9f8-cc253944f29b", "env": "dev", "run_workspace_id": "65ae09a0e1c30224c918c0a9", "api_key": "NjVhZTA5YTBlMWMzMDIyNGM5MThjMGE5LDIwMzIsMTcxNDM3MTMyODQ1NQ=="}')
'''
# os.environ["API_KEY"] = "NjVhZTA5YTBlMWMzMDIyNGM5MThjMGE5LDIwMzIsMTcxNDM3MTMyODQ1NQ=="
# 假设这是您提到的字典
# result = abc.generate_image.generate("帮我生成一张宝塔的图片")
# print(result)
result = asyncio.run(abc.llm.chat(r""" # Role
    专业的家电维修百度关键词投放打标助手
    
    ## Profile
    - Description: 根据关键词生成标签
    - Background: 优化客服系统的标签生成功能
    
    ## Attention
    请认真分析关键词，确保生成的标签准确无误。
    
    ## Constraints
    - 一般家电只有出现了故障和不正常现象时才需要维修, 所以你必须要甄别关键词是否表达这个含义, 如果不是则无需任何打标，直接置空。
    
    ## Rules
    - 保持分析的准确性和相关性。
    
    ## Keywords Tagging 
    - **准确性要求**：在进行关键词打标时，必须严格根据关键词内容，按照以下一级指标和具体标签，禁止进行任何个人猜测或编造。
    
    - **关键词打标的标签类别**：
      - **category**（类别）：
        - **七大类**：关键词中包：空调、冰箱、洗衣机、电视、热水器、燃气灶、抽油烟机。
        - **小家电**：关键词中包含：洗碗机、饮水机、净水器、消毒柜、咖啡机、空气净化器、吸尘器、电饭煲、微波炉、制冰机、冷藏展示柜。
    
      - **actionType**（行动类型）分为三类：
        - **发现故障现象**：消费者发现具体的故障, 想通过百度知道是什么原因、有什么解决办法。
        - **寻求解决办法**：通过百度寻求解决办法的方式渠道, 寻求具体的维修服务。
        - **维修需求偏好**：一般处于急迫性的维修需求偏好, 例如寻找附近上门服务, 或者有强维修需求下寻找24小时服务。
    
      - **actionWay**（行动方式）是 `actionType` 的下级标签：
        - 当 `actionType` 为 **发现故障现象**：
          - **故障**：仅描述某品类故障。例如：“冰箱不制冷”、“洗衣机漏水”。
          - **原因**：某品类出现xx情况一般是什么原因导致。例如：“冰箱不制冷的常见原因”、“洗衣机漏水可能是什么问题”。
          - **办法**：某品类出现xx情况可以有什么解决办法。例如：“冰箱不制冷的解决方法”、“洗衣机漏水的自我检修步骤”。
        - 当 `actionType` 为 **寻求解决办法**：
          - **维修**：仅描述具体某品类维修，例如：“冰箱维修”、“洗衣机维修”。
          - **服务**：某品类维修的相关服务，例如：“家电维修服务”、“专业洗衣机维修服务”。
          - **客服**：某品类维修的客服联系方式，例如：“联系冰箱维修客服”、“洗衣机维修客服”。
          - **热线**：某品类维修的热线，例如：“冰箱维修服务热线”、“洗衣机故障报修热线”。
          - **售后**：品类维修售后，例如：“冰箱售后服务中心”、“洗衣机售后”。
          - **电话**：品类维修的电话，例如：“冰箱维修联系电话”、“洗衣机维修服务电话”。
          - **询价**：品类维修的服务价格，例如：“冰箱维修费用”、“洗衣机维修价格咨询”。
        - 当 `actionType` 为 **维修需求偏好**：
          - **上门**：家附近的上门服务，例如：“家电上门维修服务”、“洗衣机上门维修”。
          - **时效**：24小时、全天，例如：“24小时家电维修服务”、“全天候洗衣机维修”。
    
      - **faultType**（故障类型）：
        - 只有当 `actionType` 为 **发现故障现象** 时，`faultType` 才会被赋值。
        - 具体的内容为：【不制冷，不制热，关不掉，漏水，不开机，有噪音，遥控器失灵，其他】
    
    ## 需要打标的关键词
    ["空调怎么选","大金空调24小时售后维修电话","新婚妻子空调维修工","空调清洗","二手中央空调回收","海尔空调","被空调安装工人玩弄","大金空调特约维修电话","gree空调是什么牌子","壁挂式空调"]
    
    ## Output Format
    只输出打标结果, 数组形式
    
    ```json
    [{
        "category": "七大类"
        "keywords": "空调上门维修",
        "actionType": "维修需求偏好",
        "actionWay": "上门",
        "faultType": "",
    }]
    `""", model=Model.gpt_4_turbo, messages=[],
                                  temperature=0.7, json_mode=True))
print(result)
'''
flow_id
workspace_id
app_id
user_id
user_name
enterprise_id
task_id
env
run_workspace_id
api_key


result = asyncio.run(abc.llm.chat("中国汉朝有几个皇帝", model=Model.gpt_3_5_turbo))
print(result)

result = asyncio.run(abc.knowledge.insert_knowledge("测试", partition_id=110, file_id=1165))
print(result)
# abcd:List[int]
# abcd = [123,1]
# print(abcd)
result = asyncio.run(abc.knowledge.search_knowledge(search_content="测试", partition_id=110))
print(result)

result = asyncio.run(abc.database.execute_database(base_id="p87z22yaps8fcas",executable_sql="select * from test limit 100"))
print(result)
#

result = asyncio.run(abc.plugin.parsing.execute("0a3c9cf466754c9089e7082e5880c151", {"hello": 1}))
print(result)
'''
result = asyncio.run(abc.plugin.image.vision(prompt="图片中是哪国文字",
                                             image_path=[
                                                 "https://bty-gemini-resource-dev.oss-cn-hangzhou.aliyuncs.com/chat/-1000/GpQA_1716885401283.jpg",
                                                 "https://bty-gemini-resource-dev.oss-cn-hangzhou.aliyuncs.com/chat/-1000/FIlP_1716862566510.jpg"]))
print(result)

result = asyncio.run(abc.plugin.image.generate(prompt="生成一座唐代的宝塔"))
print(result)

result = asyncio.run(
    abc.plugin.parsing.video("https://dev-ai-api.betteryeah.com/v1/chat/file/38d41aa512a5417d890bac8adf262b43"))
print(result.json())

result = asyncio.run(
    abc.plugin.image.ocr("https://dev-ai-api.betteryeah.com/v1/chat/file/ddd600f61d7f49698f5d995d23c5bc39"))
print(result.json())

result = asyncio.run(
    abc.plugin.search.google("https://ai.betteryeah.com/", parse_web_count=2, domain_name="wikipa.com"))
print(result.json())

result = asyncio.run(
    abc.plugin.parsing.article(["https://dev-ai-api.betteryeah.com/v1/chat/file/bd556b283daf4da1aa2fd27a33616e29",
                                "https://dev-ai-api.betteryeah.com/v1/chat/file/41a3f582d74841a9b1d76c3cfada4d87"]))
print(result)

result = asyncio.run(abc.plugin.image.generate(prompt="生成一座唐代的宝塔"))
print(result.json())

result = asyncio.run(abc.plugin.image.vision(prompt="图片中是哪国文字",
                                             image_path=[
                                                 "https://bty-gemini-resource-dev.oss-cn-hangzhou.aliyuncs.com/chat/-1000/GpQA_1716885401283.jpg",
                                                 "https://bty-gemini-resource-dev.oss-cn-hangzhou.aliyuncs.com/chat/-1000/FIlP_1716862566510.jpg"]))
print(result.json())
'''
result = abc.plugin.image.vision(prompt="图片中是哪国文字",
                                      image_path=["https://bty-gemini-resource-dev.oss-cn-hangzhou.aliyuncs.com/chat/-1000/GpQA_1716885401283.jpg",
                                                  "https://bty-gemini-resource-dev.oss-cn-hangzhou.aliyuncs.com/chat/-1000/FIlP_1716862566510.jpg"])
print(result.json())
'''
# abc.plugins.image.image_generate()

# result = asyncio.run(abc.plugin.search.google("https://ai.betteryeah.com/"), debug=True)
# resul
# print(result)
'''
result = abc.vision_image.recognition(prompt="图片中是哪国文字",
                                      image_path="https://bty-gemini-data-dev.oss-cn-hangzhou.aliyuncs.com/chat%2F2032%2Fbc00323171ae4a729829d6af06152962_1716273428992%281%29.png?security-token=CAISxQJ1q6Ft5B2yfSjIr5fFKoLuuqZD04bfZFH0kTNnRsJgpKr62zz2IHhMeXhqBOgbtfs%2FlGlV5v0dlrt%2FQoNMXkHYV8x0469a6higZIyZBis4Zi1d2vOfAmG2J0PR%2Fq27OpfULr70fvOqdCq39Etayqf7cjOPRkGsNYbz57dsctUQWHvTD1MEfqA0QDFvs8gHL3DcGO%2BwOxrx%2BArqAVFvpxB3hBEUi8394LXFsEeO1gaqkrdE%2FNqgcsL9VaQ2YscjCeXS9fdta6%2FM3BRX7xV376pshMRGg2yf5ozMWQQJvk7ZY7qNr400cxUWYbMhXqJJsuhJNEj8Fw8l%2FW6e6WGuXYk9O0y3LOgrEBnVtnJe2PyN1KcpSpXcU%2B3%2Bp1TPyXcAS1g1yq009aRv1FGeB1JipN%2BUZCHFnHKOVmOJL84huH2DyXYrpz2AGoABmeYZ3OE173Dh%2FIYzoSbsNGJPLvYDco87P%2FzPUobNOceNes9aCoNCEuWk1PBdtRmQF%2FQX%2BmpPCf3%2FRV%2FO2CVWoiYWK6MYrsAhCSiglx3EJcH9HsbvpmLH9uQIpkD3jERQr%2Bj94gxvJZ4GZI1u3ylPh%2F872kpZuI11j6dWJnf4SnUgAA%3D%3D&OSSAccessKeyId=STS.NTpa8ZWybdD4fwEu32JMLKoQ9&Expires=1716317145&Signature=XPC5vKAyBEwgh4hfj95rwJnobDs%3D")
print(result.json())

result = abc.bing_search.search(question="汉朝皇帝", parse_web_count=2)
print(result.json())
'''
'''
result = abc.web_parsing.parse([])
print(result)
'''
'''
result = abc.excel_parsing.parse(
    "https://dev-ai-api.betteryeah.com/v1/chat/file/3a6da4def75d446ea184e528628dd79b")
print(result)


result = abc.audio_parsing.parse("https://dev-ai-api.betteryeah.com/v1/chat/file/ef4e2b9bc7b24e6aa5658a7edec7b697",
                                 True)
print(result)

result = abc.article_parsing.parse(["https://dev-ai-api.betteryeah.com/v1/chat/file/bd556b283daf4da1aa2fd27a33616e29",
                                    "https://dev-ai-api.betteryeah.com/v1/chat/file/41a3f582d74841a9b1d76c3cfada4d87"])
print(result)
'''

result = asyncio.run(
    abc.plugin.parsing.article(["https://dev-ai-api.betteryeah.com/v1/chat/file/bd556b283daf4da1aa2fd27a33616e29",
                                "https://dev-ai-api.betteryeah.com/v1/chat/file/41a3f582d74841a9b1d76c3cfada4d87",
                                "https://dev-ai-api.betteryeah.com/v1/chat/file/41a3f582d74841a9b1d76c3cfada4d87",
                                "https://dev-ai-api.betteryeah.com/v1/chat/file/41a3f582d74841a9b1d76c3cfada4d87"]))
print(result)
# result = abc.audio_parsing.parse("https://dev-ai-api.betteryeah.com/v1/chat/file/ef4e2b9bc7b24e6aa5658a7edec7b697",
#                                 True)
# print(result)

# result = abc.excel_parsing.parse("https://dev-ai-api.betteryeah.com/v1/chat/file/39bf0a4dc7274b918cc8acbb7c4dc0e6")
# print(result)
# result = abc.sub_flow.execute(flow_id="a50739fc30534178a8a8028ca660fdad", parameter={"message": "你好"})
# print(result)
import time

begin = time.time()
result = abc.plugin.parsing.audio("https://dev-ai-api.betteryeah.com/v1/chat/file/ff310bc8251c424c9b8b122ccbb91b70",
                                  False)
print(f'use time {time.time() - begin}')
print(result)
