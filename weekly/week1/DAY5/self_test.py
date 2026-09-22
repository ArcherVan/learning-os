class Student :
    name = ''
    age = 0
    score = 0
    count = 0
    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.score = s
        Student.count += 1
    def add_score(self, x):
        self.score += x
    def show_info(self) :
        print("姓名:%s,年龄:%d,成绩:%d" %(self.name,self.age,self.score))
    @staticmethod
    def is_pass(score):
        return score >= 60
s1 = Student("张三", 19, 85)
s2 = Student("李四", 20, 58)
s3 = Student("王五", 18, 72)
s1.add_score(10)

s1.show_info()
s2.show_info()
s3.show_info()

print(Student.count)

print(Student.is_pass(s1.score))
print(Student.is_pass(s2.score))
print(Student.is_pass(s3.score))

