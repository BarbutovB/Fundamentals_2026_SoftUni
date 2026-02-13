def calculate_price(product, quantity):
    prices = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }
    return prices[product] * quantity

input_product = input()
input_quantity = int(input())

result = calculate_price(input_product, input_quantity)
print(f"{result:.2f}")
