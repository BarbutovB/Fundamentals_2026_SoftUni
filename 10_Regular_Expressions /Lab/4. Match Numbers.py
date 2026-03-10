import re

text = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern, text)
numbers = [match.group() for match in matches]

print(" ".join(numbers))
