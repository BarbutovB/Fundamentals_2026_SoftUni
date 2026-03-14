import re

pattern = r"www\.[A-Za-z0-9\-]+(\.[a-z]+)+"

while True:
    line = input()
    if not line:
        break
        
    matches = re.finditer(pattern, line)
    for match in matches:
        print(match.group())
