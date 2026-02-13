def get_chars(start, end):
    result = []
    for i in range(ord(start) + 1, ord(end)):
        result.append(chr(i))
    return " ".join(result)

char1, char2 = input(), input()
print(get_chars(char1, char2))
