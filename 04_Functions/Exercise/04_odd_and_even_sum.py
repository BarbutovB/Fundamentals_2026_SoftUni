def get_sums(number_str):
    odd_sum = 0
    even_sum = 0
    for digit in number_str:
        num = int(digit)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return odd_sum, even_sum

input_data = input()
o_sum, e_sum = get_sums(input_data)
print(f"Odd sum = {o_sum}, Even sum = {e_sum}")
