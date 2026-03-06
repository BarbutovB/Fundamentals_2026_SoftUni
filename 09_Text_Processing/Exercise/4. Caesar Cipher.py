text = input()
encrypted_text = ""

for char in text:
    new_char = chr(ord(char) + 3)
    encrypted_text += new_char

print(encrypted_text)
