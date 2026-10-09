import json


with open("student.json", "r", encoding="utf-8") as f:
    loaded_student = json.load(f)

print(loaded_student)
print(type(loaded_student))