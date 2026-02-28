def main():
    courses_data = {}

    while True:
        entry = input()
        if entry == "end":
            break

        course_name, student_name = entry.split(" : ")

        if course_name not in courses_data:
            courses_data[course_name] = []
        
        courses_data[course_name].append(student_name)

    for course, students in courses_data.items():
        print(f"{course}: {len(students)}")
        for student in students:
            print(f"-- {student}")

if __name__ == "__main__":
    main()
