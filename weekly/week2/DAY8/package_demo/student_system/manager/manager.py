from student.student import Student
class StudentManager:
    def __init__(self):
        self.students = []

    def load_students(self,filename):
        students = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip() == '':
                        continue
                    parts = line.strip().split(",")
                    if len(parts) != 5:
                        print("数据格式错误.")
                        continue
                    try:
                        student = Student(
                            parts[0],
                            parts[1],
                            int(parts[2]),
                            int(parts[3]),
                            parts[4]
                        )
                    except ValueError:
                        print("数据类型错误.")
                        continue
                    students.append(student) 
    
        except FileNotFoundError:
            self.students = []
            return
    
        self.students = students

    def find_student(self, student_id):
        for stu in self.students:
            if stu.student_id == student_id:
                return stu
        return None

    def add_student(self, student):
        if self.find_student(student.student_id) is not None:
            return False
        self.students.append(student)
        return True

    def show_students(self):
        return self.students

    def update_student_score(self,student_id, new_score):
        student = self.find_student(student_id)
        if student is not None:
            student.score = new_score
            return True
        return False

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student is not None:
            self.students.remove(student)
            return True
        return False

    def save_students(self,filename):
        with open(filename, "w", encoding="utf-8") as f:
            for student in self.students:
                f.write(
                    f"{student.class_name},{student.name},"
                    f"{student.student_id},{student.score},{student.gender}\n"
                )


