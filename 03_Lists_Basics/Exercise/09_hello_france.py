items = input().split("|")
budget = float(input())
initial_budget = budget
new_prices = []
profit = 0

for item in items:
    type_item, price = item.split("->")
    price = float(price)
    can_buy = False

    if type_item == "Clothes" and price <= 50.00:
        can_buy = True
    elif type_item == "Shoes" and price <= 35.00:
        can_buy = True
    elif type_item == "Accessories" and price <= 20.50:
        can_buy = True

    if can_buy and budget >= price:
        budget -= price
        new_price = price * 1.40
        profit += new_price - price
        new_prices.append(new_price)

for p in new_prices:
    print(f"{p:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")

if sum(new_prices) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
