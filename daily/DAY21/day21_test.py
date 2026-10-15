from models.student import Student
from utils.student_iterator import (
    student_generator,
    passed_student_generator,
    high_id_student_generator,
    student_name_generator,
)

students = [
    Student(100, "张三"),
    Student(200, "李四"),
    Student(300, "王五"),
    Student(400, "赵六"),
]

print("全部学生：")
for student in student_generator(students):
    print(student.student_id, student.name)

print("学号大于等于250的学生：")
for student in high_id_student_generator(students):
    print(student.student_id, student.name)

print("学生姓名：")
for name in student_name_generator(students):
    print(name)