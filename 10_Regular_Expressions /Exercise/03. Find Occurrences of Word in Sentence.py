import re

sentence = input()
target_word = input()

pattern = rf"\b{target_word}\b"
matches = re.findall(pattern, sentence, flags=re.IGNORECASE)

print(len(matches))
