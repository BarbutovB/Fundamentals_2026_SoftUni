n = int(input())
magic_word = input()
strings = []

for _ in range(n):
    current_string = input()
    strings.append(current_string)

filtered_strings = []
for word in strings:
    if magic_word in word:
        filtered_strings.append(word)
print(strings)
print(filtered_strings)

