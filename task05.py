# students.json faylidan faqat 20 yoshdan katta bo‘lganlarni ekranga chiqaring.

import json

with open("students.json", "r") as jsonfile:
    students = json.load(jsonfile)

for student in students:
    if student['age'] > 20:
        print(f"{student['name']} - {student['age']} yosh")