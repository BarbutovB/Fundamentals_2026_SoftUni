products = {}

while True:
    command = input()
    if command == "statistics":
        break
    
    product, quantity = command.split(": ")
    quantity = int(quantity)

    if product not in products:
        products[product] = 0
    products[product] += quantity

print("Products in stock:")
for product, qty in products.items():
    print(f"- {product}: {qty}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
