# Talabalarni yosh bo‘yicha oshib boruvchi tartibda chiqaring.

import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

students_sorted = sorted(students, key=lambda student: student["age"])

for student in students_sorted:
    print(f"{student['name']} - {student['age']} yosh")
