import time
import concurrent.futures
from betteryeah import BetterYeah, Model

import os
# 初始化SDK
os.environ['GEMINI_SERVER_HOST'] = 'http://dev-ai-api.betteryeah.com'
betteryeah = BetterYeah(api_key="NjVhZTA5YTBlMWMzMDIyNGM5MThjMGE5LDIwMzIsMTcxNDM3MTMyODQ1NQ==")


def run_model(model, prompt):
    """
    使用指定的模型回答问题，并记录耗时。
    """
    start_time = time.time()  # 记录开始时间
    response = betteryeah.llm.chat(system_prompt=prompt, model=model)  # 使用模型进行回答
    duration = (time.time() - start_time) * 1000  # 计算耗时，转换为毫秒
    return {
        "模型名称": model.name,
        "回答结果": response.data,
        "回答耗时(毫秒)": duration
    }


def main():
    prompt = '写一个20字符的果粒橙果汁的广告词'
    models = [Model.gpt_3_5_turbo, Model.gpt_4, Model.gpt_4_turbo]
    tasks = []

    # 使用线程池来并发执行所有任务
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for model in models:
            for _ in range(3):  # 每个模型执行三次
                tasks.append(executor.submit(run_model, model, prompt))

        results = [task.result() for task in concurrent.futures.as_completed(tasks)]

    return results


if __name__ == "__main__":
    results = main()
    for result in results:
        print(result)
