import asyncio
import json

from betteryeah import Model, OutPutType, HitStrategyType
from test_base import better_yeah

datas = {
    "Apple": 98,
    "XiaoMi": 90,
    "HuaWei": 92,
    "Oppo": 88
}

result = asyncio.run(
    better_yeah.plugin.generic.chart_plotting(requirements="按照各个手机品牌的受欢迎统计数据绘制一个柱形图",
                                              data_desc="各个手机品牌受欢迎程度统计结果数据",
                                              data=json.dumps(datas)))
print(result)
result = asyncio.run(
    better_yeah.plugin.generic.chart_plotting(requirements="按照各个手机品牌的受欢迎统计数据绘制一个柱形图",
                                              data_desc="各个手机品牌受欢迎程度统计结果数据",
                                              excel_file="https://resource.bantouyan.com/betteryeah/temp/data_example.xlsx"))
print(result)

"KNOWLEDGE"
"插入"
result = asyncio.run(better_yeah.knowledge.insert_knowledge("测试", partition_id=375, file_id=1654))
print(result)
"查询"
result = asyncio.run(better_yeah.knowledge.search_knowledge(
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
result = asyncio.run(better_yeah.database.execute_database(
    base_id="base_id",
    executable_sql="select * from test limit 100"
))
print(result)

"LLM"
result = asyncio.run(better_yeah.llm.chat(
    '中国的汉朝有几位皇帝',
    json_mode=False,
    model=Model.gpt_3_5_turbo,
    messages=[],
    temperature=0.0
))
print(result)
