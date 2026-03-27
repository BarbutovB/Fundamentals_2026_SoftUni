def solve():
    line = input()
    tokens = line.split()
    total_sum = 0.0

    for token in tokens:
        first_char = token[0]
        last_char = token[-1]
        number = float(token[1:-1])

        if first_char.isupper():
            pos = ord(first_char) - ord('A') + 1
            number /= pos
        else:
            pos = ord(first_char) - ord('a') + 1
            number *= pos

        if last_char.isupper():
            pos = ord(last_char) - ord('A') + 1
            number -= pos
        else:
            pos = ord(last_char) - ord('a') + 1
            number += pos

        total_sum += number

    print(f"{total_sum:.2f}")

if __name__ == "__main__":
    solve()
