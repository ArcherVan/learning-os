def get_names():
    names = ["张三", "李四", "王五"]
    for name in names:
        yield name
for name in get_names():
    print(name)