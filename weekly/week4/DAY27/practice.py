def read_records(records):
    for record in records:
        try:
            value = int(record)
        except ValueError:
            print(f"跳过无效数据：{record}")
            continue

        yield value

    print("读取结束")


gen = read_records(["10", "abc", "20"])

print(next(gen))
print(next(gen))
print(next(gen))