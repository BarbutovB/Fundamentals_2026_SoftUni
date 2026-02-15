todo_list = []
for _ in range(11):
    todo_list.append("")

while True:
    entry = input()
    if entry == "End":
        break
    
    parts = entry.split("-")
    priority = int(parts[0])
    task = parts[1]
    
    todo_list[priority] = task

final_tasks = []
for t in todo_list:
    if t != "":
        final_tasks.append(t)

print(final_tasks)
