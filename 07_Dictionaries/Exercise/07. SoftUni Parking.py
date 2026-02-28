def main():
    n = int(input())
    parking_registry = {}

    for _ in range(n):
        command_args = input().split()
        action = command_args[0]
        username = command_args[1]

        if action == "register":
            license_plate = command_args[2]
            if username in parking_registry:
                print(f"ERROR: already registered with plate number {parking_registry[username]}")
            else:
                parking_registry[username] = license_plate
                print(f"{username} registered {license_plate} successfully")
        
        elif action == "unregister":
            if username not in parking_registry:
                print(f"ERROR: user {username} not found")
            else:
                parking_registry.pop(username)
                print(f"{username} unregistered successfully")

    for user, plate in parking_registry.items():
        print(f"{user} => {plate}")

if __name__ == "__main__":
    main()
