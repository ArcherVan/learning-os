records = [10, 20, 30]
def read_records(records):
    try:
        for record in records:
            try:
                yield record
            except ValueError:
                print("读取过程中发生 ValueError")
    finally:
        print("读取资源清理完成")

reader = read_records(records)
print(next(reader))
print(reader.close())
