from models.student import Student


def filter_students(students, min_id):
    for student in students:
        if student.student_id >= min_id:
            yield student

def main():
    students = [
        Student(1, "张三"),
        Student(2, "李四"),
        Student(3, "王五"),
        Student(4, "赵六"),
    ]

    result = filter_students(students, 3)

    print("生成器创建完成")

    for student in result:
        print(student)


if __name__ == "__main__":
    main()
