def decorator(func):
    def wrapper():
        print("开始执行")
        func()
        print("执行结束")
    return wrapper
def hello():
    print("hello")
new_hello = decorator(hello)
new_hello()