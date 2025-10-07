#reverse of a number
import os
os.system("cls")
a = int(input("Enter A Number To Print Its Reverse : "))
while a>0:
    L = a%10
    rev = L
    a = a//10
    print(rev,end="")
   