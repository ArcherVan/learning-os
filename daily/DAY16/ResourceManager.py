class Manager:
    def __enter__(self):
        print("获取资源")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("释放资源")
        if exc_type is ValueError:
            return False

with Manager():
    print("执行任务")
    raise ValueError("测试异常")
print("程序结束")