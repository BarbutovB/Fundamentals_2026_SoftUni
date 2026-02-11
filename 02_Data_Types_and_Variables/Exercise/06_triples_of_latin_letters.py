number_of_characters = int(input())
for first_character in range(97,97 + number_of_characters):
    for second_character in range(97,97 + number_of_characters):
        for third_character in range(97,97 + number_of_characters):
            print(f"{chr(first_character)}{chr(second_character)}{chr(third_character)}")
