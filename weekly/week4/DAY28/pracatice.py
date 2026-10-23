def read_valid_numbers(records):
    for record in records:
        try:
            value = int(record)
        except ValueError:
            print(f"跳过无效数据：{record}")
            continue

        yield value

    print("读取结束")


records = ["12", "abc", "25", "", "38", "error", "50"]
reader = read_valid_numbers(records)

for number in reader:
    print(number)