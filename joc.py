nums = eval(input())

nums_set = set(nums)
max_length = 0

for num in nums_set:
    # check if it's starting point
    if num - 1 not in nums_set:
        current = num
        length = 1
        
        while current + 1 in nums_set:
            current += 1
            length += 1
        
        if length > max_length:
            max_length = length

print(max_length)