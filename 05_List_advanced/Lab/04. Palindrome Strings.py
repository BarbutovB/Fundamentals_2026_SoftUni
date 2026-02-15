words = input().split()
target_palindrome = input()

found_palindromes = []
for w in words:
    if w == w[::-1]:
        found_palindromes.append(w)

count = 0
for p in found_palindromes:
    if p == target_palindrome:
        count = count + 1

print(found_palindromes)
print(f"Found palindrome {count} times")
