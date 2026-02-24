words = input().split()
occurrences = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in occurrences:
        occurrences[word_lower] = 0
    occurrences[word_lower] += 1

result = [word for word, count in occurrences.items() if count % 2 != 0]
print(" ".join(result))
