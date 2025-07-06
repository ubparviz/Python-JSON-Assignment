# input() yordamida foydalanuvchidan ism, familiya, yosh so‘rang va mavjud students.json fayliga qo‘shib yozing.

import json

name = input("Ismingizni kiriting: ")
surname = input("Familiyangizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))

new_student = {"name": name, "surname": surname, "age": age}

try:
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = []

students.append(new_student)

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Yangi talaba muvaffaqiyatli qo'shildi!")
