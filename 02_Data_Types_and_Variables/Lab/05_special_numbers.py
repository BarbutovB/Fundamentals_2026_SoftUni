n = int(input())

for number in range(1, n + 1):
    digit_sum = 0
    current_number = number

    while current_number > 0:
        digit_sum += current_number % 10
        current_number //= 10

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
