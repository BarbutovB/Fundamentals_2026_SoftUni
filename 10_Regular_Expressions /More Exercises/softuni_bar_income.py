import re

pattern = r"%(?P<customer>[A-Z][a-z]+)%[^|$%.]*<(?P<product>\w+)>[^|$%.]*\|(?P<count>\d+)\|[^|$%.]*?(?P<price>\d+\.?\d*)\$"
total_income = 0

while True:
    line = input()
    if line == "end of shift":
        break
    
    match = re.search(pattern, line)
    if match:
        customer = match.group("customer")
        product = match.group("product")
        count = int(match.group("count"))
        price = float(match.group("price"))
        
        current_total = count * price
        total_income += current_total
        print(f"{customer}: {product} - {current_total:.2f}")

print(f"Total income: {total_income:.2f}")
