def main():
    count = int(input())
    grades_records = {}

    for _ in range(count):
        name = input()
        grade = float(input())

        if name not in grades_records:
            grades_records[name] = []
        
        grades_records[name].append(grade)

    for student, grades in grades_records.items():
        average = sum(grades) / len(grades)
        if average >= 4.50:
            print(f"{student} -> {average:.2f}")

if __name__ == "__main__":
    main()
