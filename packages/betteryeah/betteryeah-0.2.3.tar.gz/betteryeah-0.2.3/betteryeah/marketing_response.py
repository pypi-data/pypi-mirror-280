from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional

from betteryeah.response import BaseResponse


@dataclass
class XiaoHongShuCoverSearchResponse(BaseResponse):
    data: List[str]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = response_dict.get("data", [])


@dataclass
class XiaoHongShuPopularNotesItem:
    title: str
    url: int
    liked_count: str

    def __init__(self, response_dict: dict):
        self.title = response_dict.get("title")
        self.url = response_dict.get("url")
        self.liked_count = response_dict.get("liked_count")


@dataclass
class XiaoHongShuPopularNotesResponse(BaseResponse):
    data: Optional[list[XiaoHongShuPopularNotesItem]]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        if response_dict.get("data") is not None:
            self.data = [XiaoHongShuPopularNotesItem(i) for i in response_dict.get('data')]
        else:
            self.data = None


@dataclass
class XiaoHongShuCommentSearchResponse(BaseResponse):
    data: List[str]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = response_dict.get("data", [])


class BiliBiliHotTopicItem:
    topic: str
    url: str

    def __init__(self, response_dict: dict):
        self.topic = response_dict.get("topic")
        self.url = response_dict.get("url")


@dataclass
class BiliBiliHotTopicResponse(BaseResponse):
    data: List[BiliBiliHotTopicItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [BiliBiliHotTopicItem(i) for i in response_dict.get("data", [])]


@dataclass
class ZhihuRealtimeHotspotsItem:
    topic: str
    url: str
    heat: str
    excerpt: str

    def __init__(self, response_dict: dict):
        self.topic = response_dict.get("topic")
        self.url = response_dict.get("url")
        self.heat = response_dict.get("heat")
        self.excerpt = response_dict.get("excerpt")


@dataclass
class ZhiHuHotTopicResponse(BaseResponse):
    data: List[ZhihuRealtimeHotspotsItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [ZhihuRealtimeHotspotsItem(i) for i in response_dict.get("data", [])]


@dataclass
class DouyinCommentsResponse(BaseResponse):
    data: List[Dict[str, str]]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = response_dict.get("data", [])


@dataclass
class DouyinVideoAnalysisItemDetail:
    startTime: int
    endTime: int
    text: str
    image: str

    def __init__(self, item: Dict[str, any]):
        self.startTime = item.get("startTime")
        self.endTime = item.get("endTime")
        self.text = item.get("text")
        self.image = item.get("image")


@dataclass
class DouyinVideoAnalysisItem:
    title: Optional[str]
    tags: Optional[List[str]]
    data: Optional[List[DouyinVideoAnalysisItemDetail]]

    def __init__(self, response_dict: dict):
        self.title = response_dict.get("title")
        self.tags = response_dict.get("tags")
        self.data = [DouyinVideoAnalysisItemDetail(item) for item in response_dict.get("data")]


@dataclass
class DouyinVideoAnalysisResponse(BaseResponse):
    data: Optional[DouyinVideoAnalysisItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        if response_dict.get("data") is not None:
            self.data = DouyinVideoAnalysisItem(response_dict.get("data"))
        else:
            self.data = None


@dataclass
class WeiboHotspotItem:
    title: str
    heat: int
    category: str

    def __init__(self, hotspot: Dict[str, any]):
        self.title = hotspot.get("topic")
        self.heat = hotspot.get("heat")
        self.category = hotspot.get("category")


@dataclass
class WeiboHotspotsResponse(BaseResponse):
    data: List[WeiboHotspotItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [WeiboHotspotItem(item) for item in response_dict.get("data", [])]


@dataclass
class XiaoHongShuHotspotItem:
    topic: str
    heat: str
    relatedHottestNote: Dict[str, any]

    def __init__(self, hotspot: Dict[str, any]):
        self.topic = hotspot.get("topic")
        self.heat = hotspot.get("heat")
        self.relatedHottestNote = {
            "title": hotspot["relatedHottestNote"].get("title"),
            "mainBody": hotspot["relatedHottestNote"].get("mainBody"),
            "tags": hotspot["relatedHottestNote"].get("tags"),
            "comments": hotspot["relatedHottestNote"].get("comments")
        }


@dataclass
class XiaoHongShuHotTopicResponse(BaseResponse):
    data: List[XiaoHongShuHotspotItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [XiaoHongShuHotspotItem(item) for item in response_dict.get("data", [])]


@dataclass
class XiaoHongShuHotTopicResponse(BaseResponse):
    data: List[str]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = response_dict.get("data", [])


@dataclass
class XiaoHongShuCommentItem:
    content: str
    create_time: str
    like_count: int
    sub_comments: List['XiaoHongShuCommentItem'] = field(default_factory=list)

    def __init__(self, comment: Dict[str, any]):
        self.content = comment.get("content")
        self.create_time = comment.get("create_time")
        self.like_count = comment.get("like_count")
        self.sub_comments = [XiaoHongShuCommentItem(sub) for sub in comment.get("sub_comments", [])]


@dataclass
class XiaoHongShuCommentResponse(BaseResponse):
    data: List[XiaoHongShuCommentItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [XiaoHongShuCommentItem(item) for item in response_dict.get("data", [])]


@dataclass
class XiaoHongShuNoteDetailItem:
    title: str
    desc: str
    url: str
    id: str
    image: str
    imageList: List[str]
    likes: int
    comments: int
    collects: int
    shareCount: int
    tags: List[str]

    def __init__(self, note_details: Dict[str, any]):
        self.title = note_details.get("title")
        self.desc = note_details.get("desc")
        self.url = note_details.get("url")
        self.id = note_details.get("id")
        self.image = note_details.get("image")
        self.imageList = note_details.get("imageList", [])
        self.likes = note_details.get("likes", 0)
        self.comments = note_details.get("comments", 0)
        self.collects = note_details.get("collects", 0)
        self.shareCount = note_details.get("shareCount", 0)
        self.tags = note_details.get("tags", [])


@dataclass
class XiaoHongShuNoteDetailResponse(BaseResponse):
    data: XiaoHongShuNoteDetailItem

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        if response_dict.get("data"):
            self.data = XiaoHongShuNoteDetailItem(response_dict["data"])
        else:
            self.data = XiaoHongShuNoteDetailItem({})


class DouyinHotspotsType(Enum):
    hot = "热榜"
    entertainment = "娱乐榜"
    society = "社会榜"
    challenge = "挑战榜"


@dataclass
class DouyinHotspotItem:
    topic: str
    url: str
    heat: int

    def __init__(self, hotspot: Dict[str, any]):
        self.topic = hotspot.get("topic")
        self.url = hotspot.get("url")
        self.heat = hotspot.get("heat")


@dataclass
class DouYinHotTopicResponse(BaseResponse):
    data: List[DouyinHotspotItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [DouyinHotspotItem(item) for item in response_dict.get("data", [])]


@dataclass
class XiaoHongShuNoteItem:
    url: str
    liked_count: int
    author_name: str
    author_id: str
    fan_count: int
    liked_fan_rate: float

    def __init__(self, note_details: Dict[str, any]):
        self.url = note_details.get("url")
        self.liked_count = note_details.get("liked_count")
        self.author_name = note_details.get("author_name")
        self.author_id = note_details.get("author_id")
        self.fan_count = note_details.get("fan_count")
        self.liked_fan_rate = note_details.get("liked_fan_rate")


@dataclass
class XiaoHongShuNoteSearchResponse(BaseResponse):
    data: List[XiaoHongShuNoteItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [XiaoHongShuNoteItem(item) for item in response_dict.get("data", [])]


@dataclass
class XiaoHongShuSearchNotesItem:
    id: str
    title: str
    url: str
    likedCount: str

    def __init__(self, item_dict):
        self.id = item_dict.get("id")
        self.title = item_dict.get("title")
        self.url = item_dict.get("url")
        self.likedCount = item_dict.get("likedCount")


@dataclass
class XiaoHongShuSearchNotesResponse(BaseResponse):
    data: Optional[List[XiaoHongShuSearchNotesItem]]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        if response_dict.get("data", []) is not None:
            self.data = [XiaoHongShuSearchNotesItem(item) for item in response_dict.get("data", []).get("list", [])]


@dataclass
class XiaoHongShuTagItem:
    tag: str
    usageFrequency: int

    def __init__(self, tag_info: Dict[str, any]):
        self.tag = tag_info.get("tag")
        self.usageFrequency = tag_info.get("usageFrequency")


@dataclass
class XiaoHongShuSearchTagResponse(BaseResponse):
    data: List[XiaoHongShuTagItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [XiaoHongShuTagItem(item) for item in response_dict.get("data", [])]


@dataclass
class XiaoHongShuVogueNoteItem:
    title: str
    url: str
    liked_count: int

    def __init__(self, note_details: Dict[str, any]):
        self.title = note_details.get("title")
        self.url = note_details.get("url")
        self.liked_count = note_details.get("liked_count")


@dataclass
class XiaoHongShuVogueNoteSearchResponse(BaseResponse):
    data: List[XiaoHongShuVogueNoteItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [XiaoHongShuVogueNoteItem(item) for item in response_dict.get("data", [])]


@dataclass
class XiaoHongShuPopularNotesSearchItem:
    url: str
    title: str
    liked_count: int
    author_name: str
    author_id: str
    fan_count: int
    liked_fan_rate: float

    def __init__(self, note_details: Dict[str, any]):
        self.url = note_details.get("url")
        self.title = note_details.get("title")
        self.liked_count = note_details.get("liked_count")
        self.author_name = note_details.get("author_name")
        self.author_id = note_details.get("author_id")
        self.fan_count = note_details.get("fan_count")
        self.liked_fan_rate = note_details.get("liked_fan_rate")


@dataclass
class XiaoHongShuPopularNotesResponse(BaseResponse):
    data: List[XiaoHongShuPopularNotesSearchItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [XiaoHongShuPopularNotesSearchItem(item) for item in response_dict.get("data", [])]


@dataclass
class XiaoHongShuAccountNoteItem:
    title: str
    url: str
    liked_count: int

    def __init__(self, note_details: Dict[str, any]):
        self.title = note_details.get("title")
        self.url = note_details.get("url")
        self.liked_count = note_details.get("liked_count")


@dataclass
class XiaoHongShuAccountNoteSearchResponse(BaseResponse):
    data: List[XiaoHongShuAccountNoteItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [XiaoHongShuAccountNoteItem(item) for item in response_dict.get("data", [])]


@dataclass
class ToutiaoHotspotItem:
    title: str
    url: str
    heat: int

    def __init__(self, hotspot: Dict[str, any]):
        self.title = hotspot.get("topic")
        self.url = hotspot.get("url")
        self.heat = hotspot.get("heat")


@dataclass
class ToutiaoTouTiaoHotTopicResponse(BaseResponse):
    data: List[ToutiaoHotspotItem]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [ToutiaoHotspotItem(item) for item in response_dict.get("data", [])]


@dataclass
class WeiboHotspotItem:
    topic: str
    heat: int
    category: str

    def __init__(self, response_dict: dict):
        self.topic = response_dict.get("topic")
        self.heat = response_dict.get("heat")
        self.category = response_dict.get("category")


@dataclass
class WeiboHotspotsResponse(BaseResponse):
    data: Optional[List[WeiboHotspotItem]]

    def __init__(self, response_dict: dict):
        super().__init__(response_dict)
        self.data = [WeiboHotspotItem(item) for item in response_dict.get('data', [])]
