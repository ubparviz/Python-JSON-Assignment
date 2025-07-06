# students.json faylidan o‘rtacha yoshni hisoblang.

import json

with open("students.json", "r") as jsonfile:
    students = json.load(jsonfile)

total_age = 0

for student in students:
    total_age += student['age']

average = total_age / len(students)
print(f"O'rtacha yosh: {average}")