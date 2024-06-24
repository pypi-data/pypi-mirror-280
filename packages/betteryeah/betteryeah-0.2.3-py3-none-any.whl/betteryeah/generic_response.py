from dataclasses import dataclass
from typing import Optional

from betteryeah.response import BaseResponse


@dataclass
class ChartPlottingResponse(BaseResponse):
    data: Optional[str]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = response_dict.get("data")
