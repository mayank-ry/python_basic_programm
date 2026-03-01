def fact(n):
    if n==1:
        return 1
    elif n>1:
       return n*fact(n-1)
    else:
        print("Meow")
        
        
print(fact(5))
