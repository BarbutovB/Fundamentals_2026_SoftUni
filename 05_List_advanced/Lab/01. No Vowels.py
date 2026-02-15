text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

result = []
for char in text:
    if char not in vowels:
        result.append(char)

print("".join(result))
