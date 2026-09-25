from manager.manager import StudentManager
from student.student import Student
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("请输入整数.")
            continue

def input_score(prompt):
    while True:
        s = input_int(prompt)
        if s < 0 or s > 100:
            print("成绩范围应为 0 到 100。")
            continue
        return s

def menu(manager):
    while True:
            print("===== 学生管理系统 =====")
            print("1. 添加学生")
            print("2. 查看所有学生")
            print("3. 修改成绩")
            print("4. 查询学生")
            print("5. 删除学生")
            print("0. 退出系统")
            choice = input("请选择操作：")
            match choice:
                case '1':
                    class_name = input("请输入班级：")
                    name = input("请输入姓名：")
                    student_id = input_int("请输入学号：")
                    score = input_score("请输入成绩：")
                    gender = input("请输入性别：")
                    student = Student( 
                        class_name,
                        name,
                        student_id,
                        score,
                        gender
                    )
                    result = manager.add_student(student)
                    if result is False:
                        print("学号已经存在，添加失败.")
                    else:
                        print("学生添加成功.")

                case '2':
                    students = manager.show_students()
                    for student in students:
                        student.show_info()
                    
                case '3':
                    student_id = input_int("请输入要修改学生的学号：")
                    score = input_score("请输入新成绩：")
                    result = manager.update_student_score(student_id,score)
                    if result is False:
                        print("学号不存在.")
                    else:
                        print("成绩修改成功.")

                case '4':
                    student_id = input_int("请输入要修改学生的学号：")
                    result = manager.find_student(student_id)
                    if result is None:
                        print("学号不存在.")
                    else:
                        result.show_info()

                case '5':
                    student_id = input_int("请输入要删除学生的学号：")
                    result = manager.delete_student(student_id)
                    if result is False:
                        print("学生不存在，删除失败.")
                    else:
                        print("学生删除成功.")
                case '0':
                    manager.save_students("daily/DAY8/students.txt")
                    print("系统退出.")
                    break
                
def main():
    manager = StudentManager()
    manager.load_students("daily/DAY8/students.txt")
    menu(manager)

if __name__ == "__main__":
    main()
