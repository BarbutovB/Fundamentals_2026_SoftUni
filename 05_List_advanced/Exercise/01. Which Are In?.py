substrings = input().split(", ")
sentences = input().split(", ")

result = []
for sub in substrings:
    for full_text in sentences:
        if sub in full_text:
            if sub not in result:
                result.append(sub)
            break

print(result)
