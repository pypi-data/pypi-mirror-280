import asyncio

from betteryeah.marketing_response import DouyinHotspotsType
from test_base import better_yeah

result = asyncio.run(
    better_yeah.plugin.douyin.analyze_video(url="https://v.douyin.com/ijpRaosx/"))
print(result)

r"""
小红书批量封面
"""
result = asyncio.run(
    better_yeah.plugin.xhs.search_covers(urls=["https://www.xiaohongshu.com/explore/665e53b60000000005005991"]))
print(result)
r"""
小红书笔记评论批量查询
"""
result = asyncio.run(
    better_yeah.plugin.xhs.search_comments(urls=["https://www.xiaohongshu.com/explore/665e53b60000000005005991"],
                                           count=1))
print(result)
r"""
小红书实时热榜
"""
result = asyncio.run(
    better_yeah.plugin.xhs.get_hot_topics())
print(result)
r"""
小红书评论洞察
"""
result = asyncio.run(
    better_yeah.plugin.xhs.get_hot_topic_comments(keyword="中国"))
print(result)
r"""
小红书获取评论
"""
result = asyncio.run(
    better_yeah.plugin.xhs.get_comments(url="https://www.xiaohongshu.com/explore/665e53b60000000005005991"))
print(result)

r"""
小红书笔记详情
"""
result = asyncio.run(
    better_yeah.plugin.xhs.get_note_details(url="https://www.xiaohongshu.com/explore/665e53b60000000005005991"))
print(result)

r"""
小红书笔记搜素
"""
result = asyncio.run(
    better_yeah.plugin.xhs.search_notes(question="中国"))
print(result)
r"""
小红书低粉爆款笔记查询
"""
result = asyncio.run(
    better_yeah.plugin.xhs.search_low_follower_popular_notes(keyword="滑板车", count=1))
print(result)

r"""
小红书封面获取
"""
result = asyncio.run(
    better_yeah.plugin.xhs.search_covers(urls=["https://www.xiaohongshu.com/explore/665e53b60000000005005991"]))
print(result)

r"""
小红书爆款笔记
"""
result = asyncio.run(
    better_yeah.plugin.xhs.search_popular_notes(keyword="中国", count=1))
print(result)

r"""
小红书热门笔记
"""
result = asyncio.run(
    better_yeah.plugin.xhs.search_account_notes(authorId="11676399263", count=1))
print(result)

r"""
抖音实时热榜
"""
result = asyncio.run(
    better_yeah.plugin.douyin.get_hot_topics(type=DouyinHotspotsType.entertainment))
print(result)

r"""
抖音获取评论
"""
result = asyncio.run(
    better_yeah.plugin.douyin.get_comments(url='https://www.douyin.com/discover?modal_id=7379122198616870144'))
print(result)

r"""
bilibili实时热榜
"""
result = asyncio.run(
    better_yeah.plugin.bilibili.get_hot_topics())
print(result)

r"""
头条实时热榜
"""
result = asyncio.run(
    better_yeah.plugin.toutiao.get_hot_topics())
print(result)

r"""
微博实时热榜
"""
result = asyncio.run(
    better_yeah.plugin.weibo.get_hot_topics())
print(result)

r"""
知乎实时热榜
"""
result = asyncio.run(
    better_yeah.plugin.zhihu.get_hot_topics())
print(result)
