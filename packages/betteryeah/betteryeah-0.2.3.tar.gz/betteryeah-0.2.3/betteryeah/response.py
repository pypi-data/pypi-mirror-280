import json
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum


@dataclass
class BaseResponse:
    code: int
    message: str
    now_time: int
    success: str
    usage: dict

    def __init__(self, response_dict: dict):
        self.set_base_result(response_dict)

    def set_base_result(self, response_dict: dict):
        self.code = response_dict.get("code")
        self.message = response_dict.get("message")
        self.success = response_dict.get("success")
        self.now_time = response_dict.get("now_time")
        if isinstance(response_dict.get("data"), dict) and response_dict.get("data").get("upgrade_consume") is not None:
            upgrade_consume = response_dict.get("data").get("upgrade_consume")
        else:
            upgrade_consume = 0
        self.usage = response_dict.get("usage", {'consume': upgrade_consume})


@dataclass
class LLMResponse(BaseResponse):
    data: [str | dict]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = response_dict.get("data")

@dataclass
class LLMAvailableModelItem:
    name: str
    model: str

    def __init__(self, response_dict: dict):
        self.name = response_dict.get("name")
        self.model = response_dict.get("model")


@dataclass
class LLMAvailableModelResponse(BaseResponse):
    data: List[LLMAvailableModelItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [LLMAvailableModelItem(i) for i in response_dict.get("data", [])]


class FileType(Enum):
    FILE = 1
    TEXT = 2
    WEBPAGE = 3
    TEMPLATE_FILE = 4
    QA = 5


class HitStrategyType(Enum):
    MIX = 1
    KEY = 2
    SEMANTICS = 3


@dataclass
class InsertKnowledgeItem:
    file_id: [int]
    partition_id: int

    def __init__(self, response_dict: dict):
        self.partition_id = response_dict.get("partition_id")
        self.file_id = response_dict.get("file_id")


@dataclass
class InsertKnowledgeResponse(BaseResponse):
    data: Optional[InsertKnowledgeItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        if response_dict.get("data") is not None:
            self.data = InsertKnowledgeItem(response_dict)
        else:
            self.data = None


@dataclass
class WebParsingItem:
    url: str
    content: str

    def __init__(self, response_dict: dict):
        self.url = response_dict.get("url")
        self.content = response_dict.get("content")


@dataclass
class WebParsingResponse(BaseResponse):
    data: Optional[List[WebParsingItem]]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        if response_dict.get("data") is not None:
            self.data = [WebParsingItem(i) for i in response_dict.get("data")]
        else:
            self.data = None


@dataclass
class KnowledgeMatchContent:
    vector_id: str
    file_id: int
    file_type: FileType
    file_name: str
    mimetype: Optional[str]
    chunk_id: int
    content: str
    keywords: List[str]
    extra_info: Dict[str, str]
    matched_keywords: List[str]
    relevance_score: Dict[str, Optional[float]]

    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return KnowledgeMatchContent(**data)


@dataclass
class SearchKnowledgeItem:
    cost_time: float
    match_contents: List[KnowledgeMatchContent]
    usage: Any
    synonym_note: Any

    def __init__(self, cost_time: float, match_contents: List[KnowledgeMatchContent], usage: Any,
                 synonym_note: Any):
        self.cost_time = cost_time
        self.match_contents = match_contents
        self.usage = usage
        self.synonym_note = synonym_note

    @staticmethod
    def from_json(response_dict: dict):
        match_contents = [KnowledgeMatchContent.from_json(json.dumps(mc)) for mc in
                          response_dict['data']['match_contents']]
        result_data = {
            'cost_time': response_dict['data']['cost_time'],
            'match_contents': match_contents,
            'usage': response_dict['data']['usage'],
            'synonym_note': response_dict['data']['synonym_note'],
        }
        return SearchKnowledgeItem(**result_data)


@dataclass
class SearchKnowledgeResponse(BaseResponse):
    data: [SearchKnowledgeItem | str]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        if response_dict.get("success"):
            if isinstance(response_dict.get("data"), str):
                self.data = response_dict.get("data")
            else:
                self.data = SearchKnowledgeItem.from_json(response_dict)
        else:
            self.data = None


@dataclass
class ExecuteDatabaseResponse(BaseResponse):
    command: str
    rowCount: int
    data: any

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.command = response_dict.get("command")
        self.rowCount = response_dict.get("rowCount")
        self.data = response_dict.get("data")


@dataclass
class GenerateImageResponse(BaseResponse):
    data: str

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = response_dict.get("data")


@dataclass
class VisionImageResponse(BaseResponse):
    data: str

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = response_dict.get("data")


@dataclass
class SearchItem:
    title: str
    url: str
    content: str
    snippet: str

    def __init__(self, response_dict: dict):
        self.title = response_dict.get("title")
        self.url = response_dict.get("url")
        self.content = response_dict.get("content")
        self.snippet = response_dict.get("snippet")


@dataclass
class SearchResponse(BaseResponse):
    data: Optional[List[SearchItem]] | str

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        if response_dict.get("data") is not None:
            if isinstance(response_dict.get("data"), str):
                self.data = response_dict.get("data")
                return
            self.data = [SearchItem(i) for i in response_dict.get("data")]


class ExcelOutputType(Enum):
    HTML = 1
    JSON = 2


@dataclass
class ExcelParsingResponse(BaseResponse):
    data: Any

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = response_dict.get("data")


@dataclass
class AudioParsingResponse(BaseResponse):
    data: Optional[str]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = response_dict.get("data")


@dataclass
class SubFlowExecuteOutput:
    # 流程id
    flow_id: str
    # 执行任务id
    task_id: str
    # 执行结果
    run_result: str
    # 执行时长
    durationTime: Any
    # 执行信息
    message: str

    status: str

    def __init__(self, response_dict: dict):
        if response_dict is not None:
            self.flow_id = response_dict.get("flow_id")
            self.task_id = response_dict.get("task_id")
            self.run_result = response_dict.get("run_result")
            self.durationTime = response_dict.get("durationTime")
            self.message = response_dict.get("message")
            self.status = response_dict.get("status")
        else:
            self.flow_id = ""
            self.task_id = ""
            self.run_result = ""
            self.durationTime = ""
            self.message = ""
            self.status = ""


@dataclass
class SubFlowResponse(BaseResponse):
    data: Optional[SubFlowExecuteOutput]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = SubFlowExecuteOutput(response_dict.get("data"))


@dataclass
class VideoParsingItem:
    begin_time: int
    end_time: int
    silence_duration: int
    speaker_id: str
    text: str
    channel_id: int
    speech_rate: int
    emotion_value: float
    image: str = None

    def __init__(self, response_dict: dict):
        self.begin_time = response_dict.get("BeginTime")
        self.end_time = response_dict.get("EndTime")
        self.silence_duration = response_dict.get("SilenceDuration")
        self.speaker_id = response_dict.get("SpeakerId")
        self.text = response_dict.get("Text")
        self.channel_id = response_dict.get("ChannelId")
        self.speech_rate = response_dict.get("SpeechRate")
        self.emotion_value = response_dict.get("EmotionValue")
        self.image = response_dict.get("image")


@dataclass
class VideoParsingResponse(BaseResponse):
    data: Optional[List[VideoParsingItem] | str]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        if response_dict.get("data") is not None:
            if isinstance(response_dict.get("data"), str):
                self.data = response_dict.get("data")
            elif isinstance(response_dict.get("data"), list):
                self.data = [VideoParsingItem(i) for i in response_dict.get("data")]
            else:
                self.data = None
        else:
            self.data = None


@dataclass
class OCRParsingResponse(BaseResponse):
    data: Optional[str]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        if response_dict.get("data") is not None:
            self.data = response_dict.get("data")
        else:
            self.data = None
