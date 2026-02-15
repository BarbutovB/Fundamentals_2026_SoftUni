numbers_as_str = input().split(", ")
nums = []
for n in numbers_as_str:
    nums.append(int(n))

even_indices = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        even_indices.append(i)

print(even_indices)
