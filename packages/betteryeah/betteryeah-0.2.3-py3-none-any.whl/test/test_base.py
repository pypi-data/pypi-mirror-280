import os

from betteryeah import BetterYeah

os.environ['GEMINI_SERVER_HOST'] = 'https://dev-ai-api.betteryeah.com'

API_KEY = "NjVhZTA5YTBlMWMzMDIyNGM5MThjMGE5LDIwMzIsMTcxNDM3MTMyODQ1NQ=="
better_yeah = BetterYeah(api_key=API_KEY)

if API_KEY == "api_key":
    raise Exception("请先设置有效的API KEY")
