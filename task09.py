# students.json faylidagi talabalarning umumiy sonini aniqlang.

import json

with open("students.json", "r") as jsonfile:
    students = json.load(jsonfile)

print(f"Talabalarning umumiy soni: {len(students)} ta")