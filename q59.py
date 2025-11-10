import os
os.system("cls")
'''import os
os.system("cls")
numbers = []
for i in range (10):
    a = int(input(f"Enter Number {i+1} : "))
    numbers.append(a)
   
print("List Is : ",numbers)

for i in range(a):
 if a%13==0:
  print("Number Is : ",a)
  break
 else:
  print("Not Found")'''
#for i in range(1,101):
#   print(i,end=" ")

'''for i in range(1,16):
    print(i**2,end=" ")'''

'''n = int(input("enter number to print table : "))
for i in range(10):
    print(f"{n}*{i+1} = {n*i}\n")'''


'''for i in range(1,31):
    if i%3==0:
        pass
    else:
        print(i)'''

'''a = []

for i in range(10):
 num = list(map(int,input("Enter 10 Numbers : ")))
 num.append(a)
 a(num)

print(a)'''
'''sum = 0
for i in range(10):
    num = int(input(f"Enter Number {i+1} : "))
    if num>0:
        sum +=num
    else:
        pass
print(sum)'''

'''for i in range(10):
    num = int(input(f"Enter Number {i+1} : "))
    if num%13==0:
        break
    else:
        pass
print(num)'''


'''while True:
    a = int(input("Enter The Number : "))
    if a<0:
        print("Num Is Negative")
        break
    else:
        pass'''

'''for i in range(5):
    for i in range(i):
     print("*",end=" ")
    print()'''
'''
print("------------ SignUp ------------")
user = input("Enter User_Name : ")
password = input("Enter Your Password : ")

for i in range(3):
  print("------------ Login ------------")
  user1 = input("Enter Your User_Name : ")
  password1 = input("Enter Your Password : ")
  if user1==user and password1==password:
        print("Login Succesful")
        break
  else:
     print("Wrong USer/Password")
else:
    print("Attemt Is Over Now")'''
  

#wap a python prograame to check a number is whole number is  not 


'''a = int(input("Enter Number To Check : "))
if a>=0:
    print(f"Its A Whole Number : {a}")
else:
    print("Its Not A Whole Number")'''


#wap python programme given number is positive or negative

'''a = int(input("Enter A Number To Check : "))
if a>0:
    print("Its A Positive Number")
elif a<0:
    print("Its A Negative Number")
else:
    print("Its Zero")'''


#wap 4 digit number is given , you need to find max digit of the given number

'''a = int(input("Enter Number Consist Of 4 Digits : "))
while a>0:
    d1 = a%10
    n = a//10
    d2 = a%10
    n = a//10
    d3 = a%10
    n = a//10
    d4 = a%10
    n = a//10
    if d1>d2 and d1>d3 and d1>d4:
        print(f"{d1} Is Greatest")
        #break
        continue
    elif d2>d1 and d2>d3 and d2>d4:
        print(f"{d2} Is Greatest")
        #break
        continue
    elif d3>d1 and d3>d4 and d3>d4:
        print(f"{d3} Is Greatest")
        #break
        continue
    else:
        print(f"{d4} Is Greatest")
        break'''

'''a = int(input("Enter A Number : "))
max = 0
while a>0:
    rem1 = a%10
    num = a//10
    rem2 = num%10
    num = num//10
    rem3 = num%10
    num = rem2//10
    if rem1>rem2 and rem1>rem3:
        max = rem1
        print(f"({rem1} Is Greatest)")
        break
    elif rem2>rem1 and rem2>rem3:
        max = rem2
        print(f"{rem2} Is Greatest")
        break
    else:
        max = rem3
        print(f"{rem3} Is Greatest")
        break
print(max)'''

#wap to find frequency of digit in a floor digit number (repetion of same number in a digit)

#wap to find all the factors of any number (like 36 is divisible by 1,36,2,4,6,9,3) ---while or filea 

'''a = int(input("Enter A Number : "))
for i in range(1,a+1):
    if a%i==0:
        print(i,end=" ")'''



#wap to find is perfect number or not 




'''import array as arr
a = arr.array('d',[45.2,451400])
print(a)'''

'''import array as arr
a = arr.array('i',[45,41,58,63,54])
print(a)'''

'''import array as arr
a = arr.array('f',[41.5,48.2,48.6,41.5])
a.insert(2,9.5)
print(a)
a.extend([4.5,6.5])
print(a)'''

'''import array as arr
a = arr.array('i',[45,47,48,96,547,48,7,54,7,94,7,965,7])
a.remove(7)
print(a)'''

'''import array as arr
a = arr.array('i',[45,41,48,62,47,54])
print(a[::-1])'''
'''
import array as arr
a = arr.array('i',[4578,74,96,58,474,0,45,8,-1])
print(max(a))
print(min(a))'''

'''import array as arr
a =arr.array('i',[45,48,96,87,58,4,59,40])

print(a)
'''
'''import array as arr
a = arr.array('i',[44,78,74,96,44])
print(sum(a))
'''

'''import array as arr
a =arr.array('i',[45,48,59,65,41,52])
print(a)
b = int(input("Enter Number To Find Its Index : "))
if b in a:
    print(b)
    print(a.index(b))
else:
    print("Not Found")'''

tup = ("aman","blue","black","green")
print(tup)
print(tup[1])












