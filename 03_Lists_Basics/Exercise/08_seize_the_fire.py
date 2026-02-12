fire_data = input().split("#")
water = int(input())
total_fire = 0
total_effort = 0
cells_extinguished = []

for fire in fire_data:
    type_of_fire, value = fire.split(" = ")
    value = int(value)
    is_valid = False

    if type_of_fire == "High" and 81 <= value <= 125:
        is_valid = True
    elif type_of_fire == "Medium" and 51 <= value <= 80:
        is_valid = True
    elif type_of_fire == "Low" and 1 <= value <= 50:
        is_valid = True

    if is_valid and water >= value:
        water -= value
        total_fire += value
        total_effort += value * 0.25
        cells_extinguished.append(value)

print("Cells:")
for cell in cells_extinguished:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
