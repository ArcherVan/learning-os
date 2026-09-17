def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("文件不存在。")
        return None
print(read_file("not_exist.txt"))
print(read_file("daily/DAY1/scores.txt"))