from betteryeah.generic_response import ChartPlottingResponse
from betteryeah.utils import send_request


class GenericPlugin:

    async def chart_plotting(self, requirements: str, data_desc: str, data: str = None,
                             excel_file: str = None) -> ChartPlottingResponse:
        r"""
        图表插件绘制
        :param requirements:图表绘制要求，包含图表类型（折线、柱状等）、数据维度、工具栏等等图表细节信息
        :param data_desc:数据描述，即针对数据的解释，包含数据含义整体描述、字段含义、数据间逻辑关系等等信息
        :param data:用于生成图表的自定义数据源，可以是任意格式的json数据。
        :param excel_file:excel文件链接，如果用户输入中没有文件链接，默认值为空字符串
        :return 返回markdown格式的字符串
        """
        if data is None and excel_file is None:
            raise Exception("data 与 excel_file 不能同时为空")

        return await ChartPlotting().chart_plotting(requirements, data_desc, data, excel_file)


class ChartPlotting:
    async def chart_plotting(self, requirements: str, data_desc: str, data: str,
                             excel_file: str) -> ChartPlottingResponse:
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {
                    "requirment": requirements,
                    "dataDesc": data_desc,
                    "data": data,
                    "excelFile": excel_file
                },
                "name": "chat"
            }
        }
        return ChartPlottingResponse(await send_request("POST", data))
