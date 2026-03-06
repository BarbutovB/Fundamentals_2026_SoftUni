path_file = input().split("\\")
filename, extension = path_file[-1].split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")
 
#4
text = input()
encrypted_text = ""
for character in text:
    encrypted_symbol = chr(ord(character) + 3)
    encrypted_text += encrypted_symbol
print(encrypted_text)
