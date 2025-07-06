# students.json faylini students.csv fayliga aylantiring. Har bir qatorda ism, familiya, yosh bo‘lsin.

import json
import csv

with open("students.json", "r") as json_file:
    students = json.load(json_file)

with open("students.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(["name", "surname", "age"])

    for student in students:
        writer.writerow([student["name"], student["surname"], student["age"]])
