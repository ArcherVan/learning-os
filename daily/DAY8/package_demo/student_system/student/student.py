class Student:
    def __init__(self, class_name, name, student_id, score, gender):
        self.class_name = class_name
        self.name = name
        self.student_id = student_id
        self.score = score
        self.gender = gender

    def update_score(self, x):  
        self.score = x

    def show_info(self) :
        print("班级号:%s,姓名:%s,学号:%d,成绩:%d,%s" %(self.class_name,self.name,self.student_id,self.score,self.gender))

    def is_pass(self):
        return self.score >= 60
    