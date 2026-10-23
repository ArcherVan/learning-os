def read_records(records):
    try:
        for record in records:
            if record == "error":
                raise ValueError("读取记录失败")
            yield record

    except ValueError:
        print("读取过程中发生 ValueError")

    finally:
        print("读取资源清理完成")


records = [1, 2, "error", 4]
reader = read_records(records)

print("结果：", next(reader))
print("结果：", next(reader))
print("结果：", next(reader))
print("读取流程结束")