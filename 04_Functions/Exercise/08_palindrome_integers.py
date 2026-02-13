def is_palindrome(num_str):
    return num_str == num_str[::-1]

numbers = input().split(", ")
for n in numbers:
    print(is_palindrome(n))
