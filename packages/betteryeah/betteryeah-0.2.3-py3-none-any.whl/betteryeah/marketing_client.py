from typing import List

from betteryeah.marketing_response import XiaoHongShuCoverSearchResponse, XiaoHongShuCommentSearchResponse, \
    BiliBiliHotTopicResponse, ZhiHuHotTopicResponse, DouyinCommentsResponse, \
    DouyinVideoAnalysisResponse, XiaoHongShuHotTopicResponse, XiaoHongShuCommentResponse, \
    DouYinHotTopicResponse, XiaoHongShuSearchTagResponse, XiaoHongShuVogueNoteSearchResponse, \
    XiaoHongShuAccountNoteSearchResponse, ToutiaoTouTiaoHotTopicResponse, \
    WeiboHotspotsResponse, DouyinHotspotsType, XiaoHongShuNoteDetailResponse, XiaoHongShuSearchNotesResponse, \
    XiaoHongShuPopularNotesResponse
from betteryeah.utils import send_request


class XiaoHongShuCoverSearch:
    async def search_covers(self, urls: List[str]) -> XiaoHongShuCoverSearchResponse:
        r"""
        小红书笔记封面批量查询
        :param urls: 笔记链接列表
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"urls": urls},
                "name": "xhs_cover_search"
            }
        }
        return XiaoHongShuCoverSearchResponse(await send_request("POST", data))


class XiaoHongShuCommentSearch:
    async def search_comments(self, urls: List[str], count: int) -> XiaoHongShuCommentSearchResponse:
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"urls": urls, "count": count},
                "name": "xhs_comment_search"
            }
        }
        return XiaoHongShuCommentSearchResponse(await send_request("POST", data))


class BilibiliRealtimeHotspots:
    async def get_hotspots(self) -> BiliBiliHotTopicResponse:
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {},
                "name": "bilibili_realtime_hotspots"
            }
        }
        return BiliBiliHotTopicResponse(await send_request("POST", data))


class ZhihuRealtimeHotspots:
    async def get_hotspots(self) -> ZhiHuHotTopicResponse:
        """
        获取知乎实时热搜榜
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {},
                "name": "zhihu_realtime_hotspots"
            }
        }
        return ZhiHuHotTopicResponse(await send_request("POST", data))


class DouyinComments:
    async def get_comments(self, url: str) -> DouyinCommentsResponse:
        """
        通过抖音链接，获取相关评论
        :param url: 抖音视频的URL地址
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"url": url},
                "name": "douyin_comment"
            }
        }
        return DouyinCommentsResponse(await send_request("POST", data))


class DouyinVideoAnalysis:
    async def analyze_video(self, url: str) -> DouyinVideoAnalysisResponse:
        """
        通过抖音链接，获取视频文案和相关截图
        :param url: 抖音视频的URL地址
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"url": url},
                "name": "douyin_video"
            }
        }
        return DouyinVideoAnalysisResponse(await send_request("POST", data))


class XiaoHongShuHotspots:
    async def get_hotspots(self) -> XiaoHongShuHotTopicResponse:
        """
        获取小红书实时热点及相关热贴和评论
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {},
                "name": "xhs_hotspots"
            }
        }
        return XiaoHongShuHotTopicResponse(await send_request("POST", data))


class XiaoHongShuHotTopic:
    async def get_hot_topic_comments(self, keyword: str) -> XiaoHongShuHotTopicResponse:
        """
        评论洞察
        搜索关键词，得到多篇热门笔记的热评
        :param keyword: 搜索关键字
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"keyword": keyword},
                "name": "xhs_hot_topic"
            }
        }
        return XiaoHongShuHotTopicResponse(await send_request("POST", data))


class XiaoHongShuComment:
    async def get_comments(self, url: str) -> XiaoHongShuCommentResponse:
        """
        通过小红书链接，获取笔记评论数据
        :param url: 笔记的URL地址
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"url": url},
                "name": "xhs_comment"
            }
        }
        return XiaoHongShuCommentResponse(await send_request("POST", data))


class XiaoHongShuNote:
    async def get_note_details(self, url: str) -> XiaoHongShuNoteDetailResponse:
        """
        通过小红书笔记链接，获取标题、正文、封面图、轮播图、视频、点赞量、评论量、收藏量、分享量、标签信息
        :param url: 笔记的URL地址
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"url": url},
                "name": "xhs_note"
            }
        }
        return XiaoHongShuNoteDetailResponse(await send_request("POST", data))


class DouyinHotspots:
    async def get_hotspots(self, type: DouyinHotspotsType) -> DouYinHotTopicResponse:
        """
        获取抖音实时热搜榜
        :param type: 榜单类型（如“热榜”、“娱乐榜”等）
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"type": type.value},
                "name": "douyin_realtime_hotspots"
            }
        }
        return DouYinHotTopicResponse(await send_request("POST", data))


class XiaoHongShuNoteSearch:
    async def search_notes(self, question: str) -> XiaoHongShuSearchNotesResponse:
        """
        根据关键词搜索笔记，返回指定数量的笔记详情
        :param keyword: 搜索的问题
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"question": question},
                "name": "xhs_search"
            }
        }
        return XiaoHongShuSearchNotesResponse(await send_request("POST", data))


class XiaoHongShuTagSearch:
    async def search_tags(self, keyword: str) -> XiaoHongShuSearchTagResponse:
        """
        根据关键词搜索，返回最热100篇笔记的标签及其使用频率
        :param keyword: 搜索的关键词
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"keyword": keyword},
                "name": "xhs_tag"
            }
        }
        return XiaoHongShuSearchTagResponse(await send_request("POST", data))


class XiaoHongShuVogueNoteSearch:
    async def search_vogue_notes(self, keyword: str, count: int) -> XiaoHongShuVogueNoteSearchResponse:
        """
        根据搜索关键词获取小红书上的爆款（最热门）笔记，可以配置要获取的笔记数目
        :param keyword: 搜索的关键词
        :param count: 要获取的笔记数量，默认为10篇
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"keyword": keyword, "count": count},
                "name": "xhs_vogue_note"
            }
        }
        return XiaoHongShuVogueNoteSearchResponse(await send_request("POST", data))


class XiaoHongShuPopularNotesWithLowFollowerSearch:
    async def search_low_follower_hits(self, keyword: str, count: int) -> XiaoHongShuPopularNotesResponse:
        """
        搜索关键词，获取小红书上的低粉爆款笔记（低粉丝量的作者发布的爆款笔记），可以指定要获取的笔记数量，默认返回10篇
        :param keyword: 搜索的关键词
        :param count: 要获取的笔记数量
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"keyword": keyword, "count": count},
                "name": "xhs_popular_notes_low_followers"
            }
        }
        return XiaoHongShuPopularNotesResponse(await send_request("POST", data))


class XiaoHongShuAccountNoteSearch:
    async def search_account_notes(self, author_id: str, count: int) -> XiaoHongShuAccountNoteSearchResponse:
        """
        根据小红书账号ID查询该账号下最热门笔记，可以指定要获取的笔记数量
        :param author_id: 小红书账号ID
        :param count: 要获取的笔记数量
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {"authorId": author_id, "count": count},
                "name": "xhs_account_note"
            }
        }
        return XiaoHongShuAccountNoteSearchResponse(await send_request("POST", data))


class ToutiaoHotspots:
    async def get_hotspots(self) -> ToutiaoTouTiaoHotTopicResponse:
        """
        获取今日头条实时热搜榜
        """
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {},
                "name": "toutiao_realtime_hotspots"
            }
        }
        return ToutiaoTouTiaoHotTopicResponse(await send_request("POST", data))


class WeiboHotspots:
    async def fetch_hotspots(self) -> WeiboHotspotsResponse:
        """
        获取微博实时热搜榜单
        """
        # 处理 model 参数
        data = {
            "name": "EXECUTE_FLOW_PLUGIN",
            "parameters": {
                "inputs": {},
                "name": "weibo_hotspots"
            }
        }
        return WeiboHotspotsResponse(await send_request("POST", data))


class XiaoHongShuPlugin:

    async def search_covers(self, urls: List[str]) -> XiaoHongShuCoverSearchResponse:
        r"""
        小红书笔记封面批量查询
        :param urls: 笔记链接列表
        """
        return await XiaoHongShuCoverSearch().search_covers(urls=urls)

    async def search_comments(self, urls: List[str], count: int) -> XiaoHongShuCommentSearchResponse:
        r"""
        小红书评论批量查询
        :param urls: 笔记链接列表
        :param count: 返回的评论数目
        """
        return await XiaoHongShuCommentSearch().search_comments(urls=urls, count=count)

    async def get_hot_topic_comments(self, keyword: str) -> XiaoHongShuHotTopicResponse:
        r"""
        搜索关键词，得到多篇热门笔记的热评
        :param keyword: 搜索关键字
        """
        return await XiaoHongShuHotTopic().get_hot_topic_comments(keyword=keyword)

    async def get_comments(self, url: str) -> XiaoHongShuCommentResponse:
        r"""
        通过小红书链接，获取笔记评论数据
        :param url: 笔记的URL地址
        """
        return await XiaoHongShuComment().get_comments(url=url)

    async def get_note_details(self, url: str) -> XiaoHongShuNoteDetailResponse:
        r"""
        通过小红书笔记链接，获取详细信息如标题、正文等
        :param url: 笔记的URL地址
        """
        return await XiaoHongShuNote().get_note_details(url=url)

    async def search_notes(self, question: str) -> XiaoHongShuSearchNotesResponse:
        r"""
        根据关键词搜索笔记，返回指定数量的笔记详情
        :param question: 搜索的关键词
        """
        return await XiaoHongShuNoteSearch().search_notes(question=question)

    async def search_popular_notes(self, keyword: str, count: int) -> XiaoHongShuVogueNoteSearchResponse:
        r"""
        根据搜索关键词获取小红书上的爆款笔记
        :param keyword: 搜索的关键词
        :param count: 要获取的笔记数量
        """
        return await XiaoHongShuVogueNoteSearch().search_vogue_notes(keyword=keyword, count=count)

    async def search_low_follower_popular_notes(self, keyword: str, count: int) -> XiaoHongShuPopularNotesResponse:
        r"""
        获取小红书上的低粉爆款笔记
        :param keyword: 搜索的关键词
        :param count: 要获取的笔记数量
        """
        return await XiaoHongShuPopularNotesWithLowFollowerSearch().search_low_follower_hits(keyword=keyword, count=count)

    async def search_account_notes(self, author_id: str, count: int) -> XiaoHongShuAccountNoteSearchResponse:
        r"""
        根据小红书账号ID查询该账号下最热门笔记
        :param author_id: 小红书账号ID
        :param count: 要获取的笔记数量
        """
        return await XiaoHongShuAccountNoteSearch().search_account_notes(author_id=author_id, count=count)

    async def get_hot_topics(self) -> XiaoHongShuHotTopicResponse:
        r"""
        获取小红书实时热点及相关热贴和评论
        """
        return await XiaoHongShuHotspots().get_hotspots()


class DouyinPlugin:
    r"""
    抖音类插件
    """

    async def get_comments(self, url: str) -> DouyinCommentsResponse:
        r"""
        通过抖音链接，获取相关评论
        :param url: 抖音视频的URL地址
        """
        return await DouyinComments().get_comments(url=url)

    async def analyze_video(self, url: str) -> DouyinVideoAnalysisResponse:
        r"""
        通过抖音链接，获取视频文案和相关截图
        :param url: 抖音视频的URL地址
        """
        return await DouyinVideoAnalysis().analyze_video(url=url)

    async def get_hot_topics(self, type: DouyinHotspotsType = DouyinHotspotsType.hot) -> DouYinHotTopicResponse:
        r"""
        获取抖音实时热搜榜
        :param type: 榜单类型（如“热榜”、“娱乐榜”等）
        """
        return await DouyinHotspots().get_hotspots(type=type)


class ZhihuPlugin:
    r"""
    知乎类插件
    """

    async def get_hot_topics(self) -> ZhiHuHotTopicResponse:
        r"""
        获取知乎实时热搜榜
        """
        return await ZhihuRealtimeHotspots().get_hotspots()


class BilibiliPlugin:
    r"""
    Bilibili类插件
    """

    async def get_hot_topics(self) -> BiliBiliHotTopicResponse:
        r"""
        获取bilibili实时热搜榜
        """
        return await BilibiliRealtimeHotspots().get_hotspots()


class ToutiaoPlugin:
    r"""
    今日头条类插件
    """

    async def get_hot_topics(self) -> ToutiaoTouTiaoHotTopicResponse:
        r"""
        获取今日头条实时热搜榜
        """
        return await ToutiaoHotspots().get_hotspots()


class WeiboPlugin:
    r"""
    微博类插件
    """

    async def get_hot_topics(self) -> WeiboHotspotsResponse:
        r"""
        获取微博实时热搜榜单
        """
        return await WeiboHotspots().fetch_hotspots()

