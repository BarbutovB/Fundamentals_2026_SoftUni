search_string = input()
text = input()

while search_string in text:
    text = text.replace(search_string, "")

print(text)
