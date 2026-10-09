from functools import wraps
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("开始执行函数:",func.__name__)
        print("位置参数:", args)
        print("关键字参数:", kwargs)
        result = func(*args, **kwargs)
        print("函数执行完成")
        print("返回值:",result)
        return result
    return wrapper


@log
def divide(a, b):
    return a / b

result = divide(10, 2)
print("最终结果:", result)