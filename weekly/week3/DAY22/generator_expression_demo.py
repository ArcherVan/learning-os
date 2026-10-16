from models.student import Student

students = [
    Student(1, "张三"),
    Student(2, "李四"),
    Student(3, "王五"),
]

def student_generator(students):
    for student in students:
        yield student

filtered_students = (
    student
    for student in students
    if student.student_id >= 2
)
for student in filtered_students:
    print(student.student_id, student.name)