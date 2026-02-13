def calculate(operator, first_num, second_num):
    if operator == "multiply":
        return first_num * second_num
    elif operator == "divide":
        return int(first_num / second_num)
    elif operator == "add":
        return first_num + second_num
    elif operator == "subtract":
        return first_num - second_num

input_operator = input()
first = int(input())
second = int(input())

print(calculate(input_operator, first, second))
