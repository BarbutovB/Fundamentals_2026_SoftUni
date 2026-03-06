def get_letter_position(char):
    return ord(char.lower()) - ord('a') + 1

input_data = input().split()
total_sum = 0

for sequence in input_data:
    if not sequence:
        continue
    
    first_letter = sequence[0]
    last_letter = sequence[-1]
    number = int(sequence[1:-1])

    first_pos = get_letter_position(first_letter)
    if first_letter.isupper():
        number /= first_pos
    else:
        number *= first_pos
            last_pos = get_letter_position(last_letter)
    if last_letter.isupper():
        number -= last_pos
    else:
        number += last_pos
        
    total_sum += number

print(f"{total_sum:.2f}")
