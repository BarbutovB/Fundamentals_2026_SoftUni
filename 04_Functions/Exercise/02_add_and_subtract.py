def sum_numbers(a, b):
    return a + b

def subtract(result, c):
    return result - c

def add_and_subtract(a, b, c):
    res = sum_numbers(a, b)
    return subtract(res, c)

n1, n2, n3 = int(input()), int(input()), int(input())
print(add_and_subtract(n1, n2, n3))
