def input_int():
    while True:
        raw = input("输入年龄：")
        try:
            s = int(raw)
            return s
        except ValueError:
            print("请输入整数。")

def input_positive_int():
        while True:
            raw = input("输入数字：")
            try:
                s = int(raw)
            except ValueError:
                print("请输入整数。")
                continue
            if s <= 0 :
                print("请输入正整数。")
                continue
            return s

def input_age():
        while True:
            raw = input("输入年龄：")
            try:
                age = int(raw)
            except ValueError:
                print("请输入整数。")
                continue
            if age < 0 :
                print("年龄不能为负数。")
                continue
            if age == 0 :
                print("年龄必须大于0。")
                continue
            if age > 150 :
                print("年龄不能超过150。")
                continue    
            return age