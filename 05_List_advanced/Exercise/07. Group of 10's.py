numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers: 
    list_of_numbers = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {list_of_numbers}")
    numbers = [number for number in numbers if number not in list_of_numbers]
    current_group += 10
