from functools import wraps
import inspect

def type_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 获取函数的参数注解
        annotations = func.__annotations__
        all_args = inspect.getcallargs(func, *args, **kwargs)

        for arg, value in all_args.items():
            if arg in annotations:
                # 如果参数有类型注解，检查类型
                expected_type = annotations[arg]
                if not isinstance(value, expected_type):
                    raise TypeError(f"调用{func.__name__}方法的参数{arg}类型不正确,要求传入的类型为{expected_type.__name__},实际传入的类型为{type(value).__name__}")

        return func(*args, **kwargs)

    return wrapper

@type_check
def abc(a: int, b: int):
    print(a + b)

# 使用示例
abc(1, 2)  # 正确调用
abc('1', 2)  # 这会触发类型错误