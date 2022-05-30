import json
from collections import Counter

with open("students.json", "r") as read_file:
    students_new = json.load(read_file)

# Поиск учащихся в одном классе,посещающие одну секцию
students_class = {}
for student in students_new:
    key = student['Class'] + " " + student['Club']
    if students_class.get(key) is None:
        students_class[key] = list()
    students_class[key].append(student)

for k, v in students_class.items():
    if len(v) >1:
        print(k, [st['Name'] for st in v])

# По полу
for gender in students_new:
    if 'M' in gender['Gender']:
        print(gender)

# По части имени ученика
for student in students_new:
    if 'Hina' in (student['Name']):
        print(student)