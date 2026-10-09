from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("打印开始日志")
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print("函数执行出现异常:", e)
            raise
        else:
            print("函数正常执行完成")
            print("日志打印结束")
            print("函数", func.__name__, "执行完成，返回值:", result)
            return result
        
    return wrapper
@log
def divide(a, b):
    return a / b

divide(10, 0)


