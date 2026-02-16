sentence = input().split()
filtered_words = [word for word in sentence if len(word) % 2 == 0]
print("\n".join(filtered_words))
