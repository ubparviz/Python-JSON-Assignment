# Eng katta yoshli talabani toping va chiqaring.

import json

with open("students.json", "r") as jsonfile:
    students = json.load(jsonfile)

oldest_student = max(students, key= lambda user: user["age"])

print(f"Eng katta yoshli talaba: {oldest_student['name']} {oldest_student['surname']} - {oldest_student['age']} yosh")