from student import Student
from studentManager import StudentManager
def menu(manager):
    while True:
            print("===== 学生管理系统 =====")
            print("1. 添加学生")
            print("2. 查看所有学生")
            print("3. 修改成绩")
            print("4. 查询是否及格")
            print("5. 保存学生")
            print("6. 退出系统")
            choice = input("请选择操作：")
            match choice:
                case '1':
                    class_name = input("请输入班级：")
                    name = input("请输入姓名：")
                    student_id = int(input("请输入学号："))
                    score = int(input("请输入成绩："))
                    gender = input("请输入性别：")
                    student = Student( 
                        class_name,
                        name,
                        student_id,
                        score,
                        gender
                    )
                    result = manager.add_student(student)
                    if result is None:
                        print("学号已经存在，添加失败.")
                    else:
                        print("学生添加成功.")

                case '2':
                    manager.show_all_students()
                    
                case '3':
                    student_id = int(input("请输入要修改学生的学号："))
                    score = int(input("请输入新成绩："))
                    result = manager.update_student_score(student_id,score)
                    if result is None:
                        print("学号不存在.")
                    else:
                        print("成绩修改成功.")

                case '4':
                    student_id = int(input("请输入要查询学生的学号："))
                    result = manager.check_student_pass(student_id)
                    if result is None:
                        print("学号不存在.")
                    else:
                        print("是否及格:", result)

                case '5':
                    manager.save_students("daily/DAY6/students.txt")
                    
                case '6':
                    manager.save_students("daily/DAY6/students.txt")
                    print("系统退出.")
                    break
                
def main():
    manager = StudentManager()
    manager.load_students("daily/DAY6/students.txt")
    menu(manager)

if __name__ == "__main__":
    main()