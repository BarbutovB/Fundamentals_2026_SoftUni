numbers_str = input().split()
n = int(input())
numbers = [int(x) for x in numbers_str]

for _ in range(n):
    numbers.remove(min(numbers))

print(", ".join(map(str, numbers)))
