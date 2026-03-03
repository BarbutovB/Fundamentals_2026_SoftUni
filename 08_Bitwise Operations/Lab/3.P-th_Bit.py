n = int(input())
p = int(input())

shifted_number = n >> p
bit_at_position_p = shifted_number & 1

print(bit_at_position_p)
