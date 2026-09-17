students = [
    {"name": "张三", "score": 80},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 67},
    {"name": "赵六", "score": 88},
    {"name": "小明", "score": 100},
]
def calculate_average(students):
    if not students:
        return None
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)

def get_highest_student(students):
    if not students:
        return None
    highest_student = students[0]
    for student in students:
        if student["score"] > highest_student["score"]:
            highest_student = student
    return highest_student

def get_lowest_student(students):
    if not students:
        return None
    lowest_student = students[0]
    for student in students:
        if student["score"] < lowest_student["score"]:
            lowest_student = student
    return lowest_student

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"  
for student in students:
    grade = get_grade(student["score"])
    print(f'{student["name"]}:{student["score"]}，等级 {grade}')

def count_pass(students):
    if not students:
        return None
    count = 0
    for student in students:
        if student["score"] >= 60:
            count += 1
    return count

for student in students:
    name = student["name"]
    score = student.get("score")
    print(f"{name}:{score}")

print("平均分：", calculate_average(students))
print(get_highest_student(students))
print(get_lowest_student(students))
print(count_pass(students))
for student in students:
    for key, value in student.items():
        print(key, "=", value)
    print("---")