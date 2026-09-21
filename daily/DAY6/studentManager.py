from student import Student
from file import File
class StudentManager:
    def __init__(self):
        self.students = []

    def save_students(self,filename):
        File.save_students(filename, self.students)

    def load_students(self,filename):
        self.students = File.load_students(filename)

    def add_student(self, student):
        for stu in self.students:
            if stu.student_id == student.student_id:
                return None
        self.students.append(student)
        return True

    def show_all_students(self):
        for student in self.students:
            student.show_info()

    def update_student_score(self,student_id, new_score):
        for student in self.students:
            if student.student_id == student_id :
                student.update_score(new_score)
                return True
        return None

    def check_student_pass(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                return Student.is_pass(student.score)
        return None
    