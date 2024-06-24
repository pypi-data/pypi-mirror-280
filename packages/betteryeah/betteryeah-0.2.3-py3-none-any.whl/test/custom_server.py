import os
from betteryeah import BetterYeah

os.environ['API_KEY'] = "xxx"
better_yeah = BetterYeah()  # 此时，SDK会从环境变量中获取相关KEY，但是需要你在运行时将.env文件加载到环境变量中(比如使用dotenv库)
print(better_yeah)
