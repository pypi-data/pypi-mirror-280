import asyncio
import os

from betteryeah import BetterYeah
from betteryeah.marketing_response import DouyinHotspotsType

# https://dev-ai-api.betteryeah.com
# http://localhost:8001

addr = None
local = False
if local:
    addr = "http://localhost:8001"
else:
    addr = "https://dev-ai-api.betteryeah.com"
os.environ['GEMINI_SERVER_HOST'] = addr
abc = BetterYeah(api_key="NjVhZTA5YTBlMWMzMDIyNGM5MThjMGE5LDIwMzIsMTcxNDM3MTMyODQ1NQ==",
                 workspace_id="65ae09a0e1c30224c918c0a9", app_id="-1")

r"""
bilibili实时热榜
"""
result = asyncio.run(
    abc.plugin.bilibili.get_hot_topics())
print(result)

r"""
小红书热门笔记
"""
result = asyncio.run(
    abc.plugin.xiaohongshu.search_account_notes(author_id="11676399263", count=1))
print(result)

r"""
抖音实时热榜
"""
result = asyncio.run(
    abc.plugin.douyin.get_hot_topics(type=DouyinHotspotsType.entertainment))
print(result)
r"""
抖音获取评论
"""
result = asyncio.run(
    abc.plugin.douyin.get_comments(url='https://www.douyin.com/discover?modal_id=7379122198616870144'))
print(result)

r"""
bilibili实时热榜
"""
result = asyncio.run(
    abc.plugin.bilibili.get_hot_topics())
print(result)

r"""
头条实时热榜
"""
result = asyncio.run(
    abc.plugin.toutiao.get_hot_topics())
print(result)

r"""
微博实时热榜
"""
result = asyncio.run(
    abc.plugin.weibo.get_hot_topics())
print(result)

r"""
知乎实时热榜
"""
result = asyncio.run(
    abc.plugin.zhihu.get_hot_topics())
print(result)
