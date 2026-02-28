def main():
    products_price = {}
    products_quantity = {}

    while True:
        line = input()
        if line == "buy":
            break

        args = line.split()
        name = args[0]
        price = float(args[1])
        quantity = int(args[2])

        products_price[name] = price

        if name not in products_quantity:
            products_quantity[name] = 0
        products_quantity[name] += quantity

    for name in products_price:
        total_price = products_price[name] * products_quantity[name]
        print(f"{name} -> {total_price:.2f}")

if __name__ == "__main__":
    main()
