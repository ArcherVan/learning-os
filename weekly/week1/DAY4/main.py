from analyzer import analyzer

def main():
    while True:
        filename = str(input("请输入要分析的文件名："))
        try:
            analyze, allword, mostword = analyzer(filename)
            print("总单词数：", allword)
            print("最高频单词：", mostword)
            print("频次统计：", analyze)
            break
        except FileNotFoundError:
            print("文件不存在，请重新输入。")
            continue

if __name__ == "__main__":
    main()