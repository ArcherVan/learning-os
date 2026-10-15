students = [
    {"student_id": 100, "name": "张三", "score": 85},
    {"student_id": 200, "name": "李四", "score": 55},
    {"student_id": 300, "name": "王五", "score": 92},
    {"student_id": 400, "name": "赵六", "score": 60},
]

def passed_student_generator(students):
    for student in students:
        if student["score"] >= 60:
            yield student

for student in passed_student_generator(students):
    print(student["student_id"], student["name"], student["score"])