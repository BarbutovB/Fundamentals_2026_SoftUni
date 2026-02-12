gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    
    parts = command.split()
    cmd_type = parts[0]
    gift_name = parts[1]

    if cmd_type == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == gift_name:
                gifts[i] = "None"
    elif cmd_type == "Required":
        index = int(parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_name
    elif cmd_type == "JustInCase":
        gifts[-1] = gift_name

result = [g for g in gifts if g != "None"]
print(" ".join(result))
