records = [1, 2, 3, 4, 5 ]
def read_records(records):
    try:
        for data in records:
            yield data
    finally:
        print("开始清理读取资源")
        print("读取资源已清理")

generator = read_records(records)

print(next(generator))
generator.close()