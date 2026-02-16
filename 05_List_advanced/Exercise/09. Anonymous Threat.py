
data = input().split()
while True:
    line = input()
    if line == "3:1":
        break
        
    parts = line.split()
    cmd = parts[0]
    
    if cmd == "merge":
        start = int(parts[1])
        end = int(parts[2])
        
        if start < 0:
            start = 0
        if end >= len(data):
            end = len(data) - 1
            
        if start < end:
            merged_str = "".join(data[start:end + 1])
            for _ in range(end - start + 1):
                data.pop(start)
            data.insert(start, merged_str)
        
    elif cmd == "divide":
        idx = int(parts[1])
        parts_count = int(parts[2])
        
        target = data.pop(idx)
        size = len(target) // parts_count
        
        new_elements = []
        for i in range(parts_count):
            if i == parts_count - 1:
                new_elements.append(target)
            else:
                new_elements.append(target[:size])
                target = target[size:]
                
        for i in range(len(new_elements)):
            data.insert(idx + i, new_elements[i])

print(" ".join(data))
