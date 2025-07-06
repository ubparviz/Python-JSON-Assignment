import json
import os

file_name = "students.json"

if not os.path.exists(file_name):

    with open(file_name, "w") as file:
        json.dump([], file, indent=4)

    print(f"{file_name} fayli yaratildi.")

else:
    print(f"{file_name} fayli allaqachon mavjud.")
