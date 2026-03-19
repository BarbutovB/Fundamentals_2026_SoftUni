import re

n = int(input())
pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

for _ in range(n):
    barcode = input()
    if re.fullmatch(pattern, barcode):
        digits = re.findall(r"\d", barcode)
        if not digits:
            group = "00"
        else:
            group = "".join(digits)
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")
