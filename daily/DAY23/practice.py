students = [
    {"student_id": 101, "name": "张三", "score": 85},
    {"student_id": 202, "name": "李四", "score": 58},
    {"student_id": 303, "name": "王五", "score": 92},
    {"student_id": 404, "name": "赵六", "score": 76},
]


def filter_students(students, min_id, min_score):
    print("开始筛选")
    for student in students:
        if student["student_id"] >= min_id and student["score"] >= min_score:
            yield student

def student_name_generator(students):
    for student in students:
        yield student["name"]

filtered_students = filter_students(students, 202, 60)

names = student_name_generator(filtered_students)

for name in names:
    print(name)