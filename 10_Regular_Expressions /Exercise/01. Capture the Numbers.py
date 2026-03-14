import re
import sys

pattern = r"\d+"
numbers = []

for line in sys.stdin:
    matches = re.findall(pattern, line)
    if matches:
        numbers.extend(matches)

print(*(numbers))
