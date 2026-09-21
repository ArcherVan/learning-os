from student import Student
class File:
    @staticmethod
    def load_students(filename):
        students = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        parts = line.strip().split(",")
                        student = Student(
                            parts[0],
                            parts[1],
                            int(parts[2]),
                            int(parts[3]),
                            parts[4]
                        )
                        students.append(student) 

        except FileNotFoundError:
            return []

        return students
    
    @staticmethod
    def save_students(filename, students):
        with open(filename, "w", encoding="utf-8") as f:
            for student in students:
                f.write(
                    f"{student.class_name},{student.name},"
                    f"{student.student_id},{student.score},{student.gender}\n"
                )