n = int(input())
arr = list(map(int, input().split()))

result = []

for x in arr:
    result.append(x // 32)

print(result)