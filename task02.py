# Yuqoridagi students.json faylini o‘qing va har bir talabaning ismi bilan yoshi ekranga chiqsin:

import json

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    print(f"{student['name']} - {student['age']} yosh")
