nums = [int(x) for x in input().split()]
total = 0

while len(nums) > 0:
    idx = int(input())
    val = 0
    
    if idx < 0:
        val = nums.pop(0)
        nums.insert(0, nums[-1])
    elif idx >= len(nums):
        val = nums.pop(-1)
        nums.append(nums[0])
    else:
        val = nums.pop(idx)
        
    total += val
    
    for i in range(len(nums)):
        if nums[i] <= val:
            nums[i] += val
        else:
            nums[i] -= val

print(total)
