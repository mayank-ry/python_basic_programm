import os
os.system("cls")
a = abs(int(input("Enter The Number : ")))
count = 0

while a>0:
    L = a%10
    a = a//10
    count = count + 1
print(count)
