import concurrent.futures
from betteryeah import BetterYeah, Model

# 初始化SDK
better_yeah = BetterYeah()


def process_text(text):
    """
    处理单个文本段落，返回清洗后的结果
    """
    # 使用SDK调用聊天模型
    ai_res = better_yeah.llm.chat(
        system_prompt='你是一个文本总结小助手，根据用户提供的段落，言简意赅的总结其内容，每个段落依据语义提取关键词缩减到20个字符左右。',
        model=Model.gpt_3_5_turbo,  # 示例，选择3.5 turbo模型，实际可以选择其他模型
        messages=[{"role": "user", "content": text}]
    )

    # 获取AI总结的结果
    result = ai_res.data  # 假设data字段包含模型的输出

    # 将AI总结的结果持久化到知识库
    better_yeah.knowledge.insert_knowledge(
        content=result,
        file_id=1165,  # 实际要替换为你的知识库文件
        partition_id='110'  # 实际需要替换成你的知识库
    )

    return result


def main():
    long_text = """
    人工智能（AI）是计算机科学的一个分支，致力于创建能够执行通常需要人类智能的任务的系统。这些任务包括学习、推理、问题解决、感知和语言理解等

    机器学习是AI的一个子领域，通过算法和统计模型使计算机能够在没有明确编程指令的情况下从数据中学习和改进。常见的机器学习方法包括监督学习、无监督学习和强化学习。
    """

    # 通过连续换行符来拆分长文本为多个段落数组
    texts = long_text.strip().split("\n\n")

    # 使用并发执行所有清洗任务
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_text, texts))

    print(f'一共清洗了{len(results)}次，结果为：', results)
    return "OK"


if __name__ == "__main__":
    main()
