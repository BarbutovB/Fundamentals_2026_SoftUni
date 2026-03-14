import re

pattern = r"^>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)$"
bought_furniture = []
total_cost = 0

while True:
    line = input()
    if line == "Purchase":
        break
    
    match = re.search(pattern, line)
    if match:
        name, price, quantity = match.groups()
        bought_furniture.append(name)
        total_cost += float(price) * int(quantity)

print("Bought furniture:")
for item in bought_furniture:
    print(item)
print(f"Total money spend: {total_cost:.2f}")
