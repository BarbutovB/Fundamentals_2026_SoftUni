import re

n = int(input())
attacked_planets = []
destroyed_planets = []

for _ in range(n):
    encrypted_msg = input()

    key = len(re.findall(r"[starSTAR]", encrypted_msg))
    decrypted_msg = "".join(chr(ord(c) - key) for c in encrypted_msg)
    
    pattern = r"@(?P<planet>[A-Za-z]+)[^@\-!:>]*:(?P<population>\d+)[^@\-!:>]*!(?P<type>[AD])![^@\-!:>]*->(?P<soldiers>\d+)"
    match = re.search(pattern, decrypted_msg)
    
    if match:
        data = match.groupdict()
        if data["type"] == "A":
            attacked_planets.append(data["planet"])
        else:
            destroyed_planets.append(data["planet"])

print(f"Attacked planets: {len(attacked_planets)}")
for p in sorted(attacked_planets):
    print(f"-> {p}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for p in sorted(destroyed_planets):
    print(f"-> {p}")
