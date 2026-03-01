def multiply(a,b):
    if a==0 or b==0:
        return 0
    elif a==1:
        return b
    elif b==1:
        return a
    else:
        return a + multiply(a,b-1)

print(multiply(5,5))