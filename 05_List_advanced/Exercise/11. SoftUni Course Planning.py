def add_lesson(schedule: list, title: str):
    if title not in schedule:
        schedule.append(title)
    return schedule


def insert_lesson(schedule: list, title: str, index: int):
    if title not in schedule:
        schedule.insert(index, title)
    return schedule


def remove_lesson(schedule: list, title: str):
    if title in schedule:
        idx = schedule.index(title)
        schedule.pop(idx)
        if idx < len(schedule) and schedule[idx] == f"{title}-Exercise":
            schedule.pop(idx)
    return schedule


def swap_lessons(schedule: list, l1: str, l2: str):
    if l1 in schedule and l2 in schedule:
        idx1, idx2 = schedule.index(l1), schedule.index(l2)

        schedule[idx1], schedule[idx2] = schedule[idx2], schedule[idx1]
  
        ex1, ex2 = f"{l1}-Exercise", f"{l2}-Exercise"

        if ex1 in schedule:
            schedule.insert(idx2 + 1, schedule.pop(schedule.index(ex1)))
    
        if ex2 in schedule:
            schedule.insert(idx1 + 1, schedule.pop(schedule.index(ex2)))
    return schedule


def add_exercise(schedule: list, title: str):
    ex_name = f"{title}-Exercise"
    if title in schedule:
        if ex_name not in schedule:
            idx = schedule.index(title)
            schedule.insert(idx + 1, ex_name)
    else:
        schedule.append(title)
        schedule.append(ex_name)
    return schedule


lessons = input().split(", ")

while True:
    line = input()
    if line == "course start":
        break

    parts = line.split(":")
    command = parts[0]
    lesson_title = parts[1]

    if command == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif command == "Insert":
        lessons = insert_lesson(lessons, lesson_title, int(parts[2]))
    elif command == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif command == "Swap":
        lessons = swap_lessons(lessons, lesson_title, parts[2])
    elif command == "Exercise":
        lessons = add_exercise(lessons, lesson_title)

for i, lesson in enumerate(lessons, 1):
    print(f"{i}.{lesson}")
