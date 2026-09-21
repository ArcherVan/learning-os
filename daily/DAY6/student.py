class Student:
    def __init__(self,ca,n,sid,s,g):
        self.class_name = ca
        self.name = n
        self.student_id = sid
        self.score = s
        self.gender = g
    def update_score(self, x):  
        self.score = x
    def show_info(self) :
        print("班级号:%s,姓名:%s,学号:%d,成绩:%d,%s" %(self.class_name,self.name,self.student_id,self.score,self.gender))
    @staticmethod
    def is_pass(score):
        return score >= 60