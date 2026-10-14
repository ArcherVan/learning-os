students = [
    {"id": 1, "name": "张三", "score": 85},
    {"id": 2, "name": "李四", "score": 58},
    {"id": 3, "name": "王五", "score": 92},
    {"id": 4, "name": "赵六", "score": 45},
    {"id": 5, "name": "钱七", "score": 76},
]

def iter_passed_students(students):
    for student in students:
        if student["score"] >= 60:
            yield student

def iter_student_names(students):
    yield from iter_names_from_students(students)

def iter_names_from_students(students):
    for student in iter_passed_students(students):
        yield student["name"]

for name in iter_student_names(students):
    print(name)