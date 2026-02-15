wagons_count = int(input())
train = []
for _ in range(wagons_count):
    train.append(0)

while True:
    command_line = input()
    if command_line == "End":
        break
    
    parts = command_line.split()
    action = parts[0]
    
    if action == "add":
        people = int(parts[1])
        train[-1] = train[-1] + people
        
    elif action == "insert":
        index = int(parts[1])
        people = int(parts[2])
        train[index] = train[index] + people
        
    elif action == "leave":
        index = int(parts[1])
        people = int(parts[2])
        train[index] = train[index] - people

print(train)
