# Take input
records = eval(input())

count = 0

for key in records:
    arr = records[key]
    
    # Case: 0 or 1 element
    if len(arr) <= 1:
        count += 1
        continue
    
    # Check strictly increasing
    is_increasing = True
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            is_increasing = False
            break
    
    # Check same difference
    diff = arr[1] - arr[0]
    is_same_diff = True
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            is_same_diff = False
            break
    
    # Final check
    if is_increasing and is_same_diff:
        count += 1

# Output result
print(count)