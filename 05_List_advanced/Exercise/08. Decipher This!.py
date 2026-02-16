def decipher_word(word):

    digits = "".join([char for char in word if char.isdigit()])
    remaining_part = [char for char in word if not char.isdigit()]

    first_letter = chr(int(digits))

    if len(remaining_part) > 1:
        remaining_part[0], remaining_part[-1] = remaining_part[-1], remaining_part[0]

    return first_letter + "".join(remaining_part)

secret_message = input().split()
deciphered_message = [decipher_word(w) for w in secret_message]

print(" ".join(deciphered_message))
