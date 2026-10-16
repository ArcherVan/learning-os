def student_generator(students):
    for student in students:
        yield student

def passed_student_generator(students):
    for student in students:
        if student.student_id % 2 == 0:
            yield student

def high_id_student_generator(students):
     for student in students:
        if student.student_id >= 250:
            yield student

def student_name_generator(students):
     yield from student_names_from_students(students)

def student_names_from_students(students):
    for student in student_generator(students):
        yield student.name