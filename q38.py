import os
os.system("cls")

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

def aman():
 a =int(input("Enter A : "))
 b =int(input("Enter B : "))
 c =int(input("Enter C : "))
 print("Greatest Number Is : ",greatest(a,b,c))

aman()
    






