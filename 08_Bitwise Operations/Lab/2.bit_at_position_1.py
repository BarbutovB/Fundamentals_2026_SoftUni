n = int(input())

shifted_number = n >> 1
bit_at_position_1 = shifted_number & 1

print(bit_at_position_1)
