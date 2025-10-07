#sum of digits in a number
import os
os.system("cls")

a = int(input("Enter The Number : "))

sum = 0

while a>0:
 L = a%10
 sum = sum+L
 a=a//10
print("Sum Of Digits Are : ",sum)

