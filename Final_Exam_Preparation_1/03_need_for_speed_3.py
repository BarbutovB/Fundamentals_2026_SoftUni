n = int(input())
cars = {}

for _ in range(n):
    car_info = input().split('|')
    name, mileage, fuel = car_info[0], int(car_info[1]), int(car_info[2])
    cars[name] = {'mileage': mileage, 'fuel': fuel}

while True:
    line = input()
    if line == "Stop":
        break
    
    parts = line.split(' : ')
    command = parts[0]
    car = parts[1]
    
    if command == "Drive":
        distance = int(parts[2])
        needed_fuel = int(parts[3])
        
        if cars[car]['fuel'] < needed_fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= needed_fuel
            print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
            
            if cars[car]['mileage'] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]
                
    elif command == "Refuel":
        refill = int(parts[2])
        old_fuel = cars[car]['fuel']
        cars[car]['fuel'] = min(75, cars[car]['fuel'] + refill)
        actual_refilled = cars[car]['fuel'] - old_fuel
        print(f"{car} refueled with {actual_refilled} liters")
        
    elif command == "Revert":
        km = int(parts[2])
        cars[car]['mileage'] -= km
        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {km} kilometers")

for car, info in cars.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")
