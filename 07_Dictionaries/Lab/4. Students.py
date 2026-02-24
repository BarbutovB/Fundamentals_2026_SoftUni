students_data = []
while True:
    line = input()
    if ":" not in line:
        target_course = line.replace("_", " ")
        break
    students_data.append(line.split(":"))

for name, s_id, course in students_data:
    if course == target_course:
        print(f"{name} - {s_id}")
