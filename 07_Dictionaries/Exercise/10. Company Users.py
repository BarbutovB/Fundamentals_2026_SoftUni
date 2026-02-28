def main():
    companies = {}

    while True:
        entry = input()
        if entry == "End":
            break

        name, employee_id = entry.split(" -> ")

        if name not in companies:
            companies[name] = []
        
        if employee_id not in companies[name]:
            companies[name].append(employee_id)

    for name, employees in companies.items():
        print(name)
        for emp_id in employees:
            print(f"-- {emp_id}")

if __name__ == "__main__":
    main()
