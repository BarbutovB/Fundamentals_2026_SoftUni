n = int(input())
b = input()

binary_representation = bin(n)[2:]
count = binary_representation.count(b)

print(count)
