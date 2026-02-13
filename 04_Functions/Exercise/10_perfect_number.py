def is_perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    if divisors_sum == n:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(is_perfect(number))
