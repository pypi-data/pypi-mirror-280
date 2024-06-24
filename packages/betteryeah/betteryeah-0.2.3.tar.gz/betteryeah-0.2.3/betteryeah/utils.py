import inspect
import os
from functools import wraps
from typing import get_origin, get_args, Union

import aiohttp


async def send_request(method: str, data: dict, endpoint: str = "/integration", stream: bool = False):
    if data.get("run_args") is None and os.getenv("RUN_ARGS"):
        data["run_args"] = os.getenv("RUN_ARGS")
    headers = {
        "Authorization": f"{os.getenv('API_KEY')}",
        "Content-Type": "application/json"
    }
    base_url = "https://api.betterai.com/v1" if os.environ.get("GEMINI_SERVER_HOST") is None else os.getenv(
        "GEMINI_SERVER_HOST") + "/v1"
    url = f"{base_url}{endpoint}"
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, json=data, headers=headers) as response:
            # 根据需要处理流式传输
            if stream:
                return await response.content.read()
            else:
                return await response.json()


def type_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        all_args = inspect.getcallargs(func, *args, **kwargs)

        def check_type(val, exp_type):
            if val is None:
                # 如果值是None，只有在类型是Optional时才是合法的
                return get_origin(exp_type) is Union and type(None) in get_args(exp_type)
            origin = get_origin(exp_type)
            if origin is Union:
                # 如果类型是Union，检查是否至少有一个类型匹配
                return any(check_type(val, t) for t in get_args(exp_type))
            elif origin:
                # 处理其他泛型类型，如List或Dict
                if not isinstance(val, origin):
                    raise TypeError(
                        f"调用{func.__name__}方法的参数{arg}类型不正确,要求传入的类型为{origin.__name__},实际传入的类型为{type(val).__name__}")
                args_type = get_args(exp_type)
                if args_type and not all(check_type(item, args_type[0]) for item in val):
                    return False
                return True
            else:
                # 非泛型类型检查
                if not isinstance(val, exp_type):
                    raise TypeError(
                        f"调用{func.__name__}方法的参数{arg}类型不正确,要求传入的类型为{exp_type.__name__},实际传入的类型为{type(val).__name__}")
                return True

        for arg, value in all_args.items():
            expected_type = annotations.get(arg)
            if expected_type is None:
                continue  # 如果没有类型注解则跳过

            # 进行类型检查
            if not check_type(value, expected_type):
                raise TypeError(f"调用{func.__name__}方法的参数{arg}不符合类型要求。")

        return func(*args, **kwargs)

    return wrapper
