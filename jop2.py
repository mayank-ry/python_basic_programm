num = list(map(float , input().split()))
result = []
for n in num:
    if n>0:
        n = int(n//1)
        print(n, end=' ')
        