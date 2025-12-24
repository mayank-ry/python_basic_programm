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

'''tup = ("aman","blue","black","green")
print(tup)
print(tup[1])'''

'''a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))
a_fact = []
b_fact = []
for i in range(1,a+1):
    if a%i==0:
       a_fact.append(i)
print(f"HCF Of {a} Are : ",a_fact)
for j in range(1,b+1):
    if b%j==0:
        b_fact.append(j)
print(f"HCF Of {b} Are : ",b_fact)

while (a_fact!=1 and b_fact!=1):
    if i in b_fact:
        common_fact.append(i)
print(common_fact)'''
'''for num in range(1,max(len(a_fact),len(b_fact))+1):
    if num==i==j:
        common_fact.append(i)'''
'''common_fact = [x for x in a_fact if x in b_fact]
print(common_fact)
print(f"GCD of {a} and {b} is : ",max(common_fact))'''



'''student = {
    "st1":{
    "name" : "Aman",
    "age" : 12,
    "Sex" : "Male"
    },
    "st2":{
        "name" : "Mayank",
        "age" : 18,
        "Sex" : "Male"
    },
    "st3":{
        "name":"Kardick",
        "age" : -10,
        "sex" : "Sabse"
    }
}'''
'''for key in student:
    print(student[key])
print("-"*10)

for value in student.values():
    print(value)
print("-"*10)

for value in student.items():
    print(value)
print("-"*10)'''

'''print(student["st1"]["Sex"])
print("--"*12)
for key in student:
    print(key)
for value,key in student.items():
    print(value,key)
for key in student.values():
    print(key)
print("\n")
print(student["st1"])'''


'''s1 = {"meow",45,True,"Bh"}
s2 = {"tu",45}
#s1.add("Hello")
print(s1.union(s2))
print(s1.intersection(s2))
print(s1|s2)
print(s1&s2)
print(s1^s2)
print(s1-s2)'''

'''student = {
    "Name" : "Mayank",
    "Age" : 18,
    "Sex" : "Male"
}
print("Students Detail : ",student)'''

'''b = int(input("Enter The Base Number : "))
p = int(input("Enter Power : "))
print(f"Exponentiation Of {b} Is : ",b**p)
'''
'''import array as arr
a = arr.array('i',[])
n = int(input("Enter No. Of Elements : "))
for num in range(n):
    num = int(input("Enter Elements : "))
    a.append(num)
print(a)
user = int(input("Enter A Number To Search In Array : "))
for i in range(n):
    if a[i]==user:
        set = 1
        break
if set==1:
    print(f"{user} Found At {i+1} Index")
else:
    print("Not Found")'''
'''
a = list(map(int , input("Enter Elements : ").split()))
print("Array : ",a)
print("Maximum Of a Is : ",max(a))'''

'''a = list(map(int , input("Enter Elements Of Array : ").split()))
print(a)
a.sort()
print("Sorted Array Is : ",a)
n = int(input("Enter Number To Search : "))
low = 0
high = len(a) - 1
while low<=high:
    mid = (low+high)//2
    if a[mid]==n:
        print(f'{n} Found At {mid}')
        break
    elif a[mid]>n:
        low = mid -1
    else:
        low = mid + 1'''

'''
wap to make atm : validate atm pin (pin is correct)
after three attempt block the card
pin = 0069
'''
'''pin = 1234
j = 2
flag = 0
for i in range(1,4):
    n = int(input("Enter The Pin : "))
    if n==pin:
        print("Pin IS Correct")
        break
    else:
        print(f"Pin Is Incorrect , U Only Have {j} Attempt Left")
        j-=1
        flag = 3
if flag==3:
 print("Your Card Has Been Blocked")'''


'''a = list(map(int , input("Enter The Elements : ").split()))
result = a[0]
print(a)
for i in range(1,len(a)):
    if i%2==0:
       result+=a[i]
    else:
        result-=a[i]
print(result)'''
'''
a = list(map(int,input("Enter 10 Numbers Between (1-100) : ").split()))
even_idx = []
even_elem = []
fi_la_elem = []
for i in range(len(a)):
    if i%2==0:
        even_idx.append(a[i])
print("Element On Even Index : ",even_idx)
for num in a:
    if num%2==0:
        even_elem.append(num)
print("Elements Are Even : ",even_elem)
print("Reverse Is : ",a[::-1])

a[0],a[len(a)-1] = a[len(a)-1],a[0]
print("After Swap Both Elements : ",a)'''

# an = a+(n-1)d
'''name = ["Ram" , "Bhavesh","Akash","Keshav","Vikas","Abhinav"]
name.append("Anand")
print(name)'''


'''n = int(input("Enter Number To Print Perfect Till That :"))
number = []
for num in range(2,n+1):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:        
     number.append(i)
print(number)
'''

'''a = {
    "name" : "Mayank",
    "classs" : 10,
    "age" : 20

}
print(a)'''

'''student = {
    "Name" : "Mayank",
    "Class" : 10,
    "Roll" : 1001
}
print("The Name Is : ",student["Name"])'''

'''student = {
    "Name" : "Mayank",
    "Class" : 10,
    "Roll" : 1001
}
student["Name"] = "Aman"
print(student["Name"])
print(student)
student.update({"Sex":"Male"})
print(student)'''
'''student = {
    "Name":"Aman",
    "Class" : 11,
    "Age" : 18
}
student.pop("Class")
print(student)
student.update({"Meow":"Sex"})
student.update({"Gender" : "Hug"})
print(student)
student.popitem()
print(student)'''
'''student = {
    "Name" : "The Name",
    "Class" : 2,
    "Gender" : "Men",
    "Hate" : "Womens",
    "Age" : 10
}
if "Age" in student:
    print(student["Age"])
else:
    print("Not Found")'''
'''
student = {
    "name" : "aman",
    "class" : 10,
    "branch" : "PCB",
    "Gender" : "Male",
    "Add" : "indore"
}
print(student)

student["bhok"]="meee"
student.update({"ham":"sath"})
print(student)'''

'''chhatra = {"student_1":{"name":"Mayank","class":10,"marks":180},
           "student_2":{"name":"aman","class":11,"marks":110},
           "student_3":{"name":"gunja","class":12,"marks":22}}
print(chhatra)
max_marks = 0
for i in chhatra.values():
    if i["marks"]>max_marks:
        max_marks=i["marks"]
        student = i["name"]
print(f"{student} Scored Maximum Mark i.e {max_marks}")'''

'''employ = {
    "Mayank" : {"Salary" : 12540,"EID" : 102,"Age" : 18},
    "Aman" : {"Salary":10850,"EID":103,"Age":19},
    "Gunja" : {"Salary":405,"EID":104,"Age":24}
}
print(employ)
print("*"*60)
employ.update({"Chanda":{"Salary":750,"EID":105,"Age":21}})
print(employ)
print("*"*60)
avg_salary=0
sum_sal = 0
print("Length Of Employ Dict Is : ",len(employ))
print("*"*60)
for details in employ.values():
    sum_sal += details["Salary"]
avg_salary=sum_sal/len(employ)
for name,details in employ.items():
 if details["Salary"]>avg_salary:
    print(f"Greater Than Average Salary Of {name} i.e {details["Salary"]}")
print("Average Salary Of Employ Is : ",avg_salary)
print("*"*60)
print("Sum Of Salary Is : ",sum_sal)
print("*"*60)'''

'''students = {
    "Mayank" : {"Hindi":78,"English":89,"Math":96},
    "Aman" : {"Hindi":56,"English":63,"Math":55},
    "Chanda" : {"Hindi":65,"English":44,"Math":46},
    "Gunja" : {"Hindi":76,"English":52,"Math":94}
}
sum_marks = 0
avg_marks = 0
for name,details in students.items():
   
    sum_marks=sum(details.values())
    avg_marks=sum_marks//len(details.keys())
    print(f"Total Marks Of {name} Is {sum_marks} And Average Is {avg_marks}")
    print("~"*80)'''

'''store = {
    "Grocery" : {"Rice" : 1680,"Dal" : 3000,"Atta":865,"Sugar":3160},
    "Fruit" : {"Mango": 1610,"Apple":6520,"Muli":610},
    "Wine" : {"Plain":85,"Masala":4800,"Rum":610,"Whiskey":865} 
}
for section_name , product_detail in store.items():
    #print(section_name,product_detail)
    for product_name,price in product_detail.items():
     print(f"Price Of {product_name} is {price}")
     print("_"*60)
     if price>1000:
        new_price=price-price/10
        store[section_name][product_name] = new_price
        print(f"Updated Price Of {product_name} is {new_price}")
        print("_"*60)
print(store)
print("_"*60)'''

'''mewo = {14,14,"Meow",784,True}
for i in mewo:
    print(i,end = " ")'''
'''a = [1,2,3,3,4,5,1,6]
a_copy = set(a)
print(a_copy)
print(list(a_copy))
print(type(a))'''
'''e1 = {"Python","SQL","C"}
e2 = {"Python","Java","HTML"}

print("Common Skills Are : ",e1 & e2)
print("Unique In E1 : ",e1-e2)
print("Unique In E2 : ",e2-e1)
print("Required In COmpany : ",e1|e2)
print("Skills Not Common : ",e1^e2)'''

'''cricket = {"A","B","C","D"}
football = {"B","D","E"}
badminton = {"A","D","F"}

two_sports = (cricket & football) | (cricket & badminton) | (cricket & badminton)
three_sprts = cricket & football & badminton
exact = two_sports - three_sprts
print(exact)'''
'''print("-"*60)
passed = {"A","B","C","D"}
failed = {"E","F","B"}
student_both = (passed & failed)
print("Students Who Passed As Well As Failed : ",student_both)
student_passed = (passed - failed)
print("Student Only Passed : ",student_passed)
print("All Unique Student : ",set(passed|failed))'''
print("-"*60)
#count unique words
'''paragraph = """
Python is powerful. Python is easy to learn and Python is widely used in programming.
"""
words = paragraph.lower().split()
print(words)
print(set(words))
print(len(set(words)))'''

'''ips = [
    "192.168.1.1", "10.0.0.2", "192.168.1.1",
    "10.0.0.3", "10.0.0.2", "172.16.0.5"
]
unique = set(ips)
print("Unique Ips Are : ",unique)
print("Total Unique Ips Visited : ",len(unique))'''

'''x= int(input("Enter Numbers : "))
try : 
 meow = lambda n : n**2
 print(meow(x))
except Exception as e:
 print(e)

print("lachlach lach")'''


'''try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter Number B : "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Number Can't Divide By Zero")
except ValueError:
    print("Invalid Value , Is'nt a int")
except Exception as e:
    print(e)

print("meow")'''
'''list = [10,20,30]
try:
    n = int(input("Enter A Index : "))
    print("Value Is : ",list[n])
except IndexError:
    print("Index Error , Out Of Index")
except Exception as e:
    print(e)
else:
    print("Not A Bug Found")
print("bye-Bye")'''
'''
try:
    a=int(input("Enter Number A : "))
    b = int(input("Enter B : "))
    print("Sum Is : ",a+b)
except ValueError:
    print("Inappropriate Type , Make Sure U Enter An Int")
print("NNN")'''

'''try:
    a = int(input("Enter Number A : "))
    b = int(input("Enter B : "))
    c = a/b
except ZeroDivisionError:
    print("Zero Division Not Possible")
print("Bye Bye")'''

'''try:
    a = int(input("Enter An Integer Number : "))
except ValueError:
    print("Please Enter An Integer")
print("Bye Bye")'''
'''try:
 a = list(map(int,input("Enter Elements : ").split()))
 print(a)
 n = int(input("Enter Index To Print : "))
 print(a[n])
except IndexError:
 print("Index Error , Out Of Range Index")
finally:
 print("Nothing Meow")'''

'''try:
    a = input("Enter A String : ")
    b = int(a)
    print(b)
except ValueError:
    print("It Doesnt Converts Into Int")'''

'''try:
    a = int(input("Enter A : "))
    b = int(input("Enter B : "))
    c = a/b
    print("C Is : ",c)
except ZeroDivisionError:
    print("Is'nt Divide By Zero")
except ValueError:
    print("Invalid Input")
finally:
    print("Bye Bye")
'''
'''try:
    a = input("Enter Element : ")
    b = int(a)
    print(b)
except ValueError:
    print("Invalid Type ")
else:
    print("valid Input")
finally:
    print("Code Done Succesfully")'''
'''try:
 student = {
    "Mayank" : 110,
    "Meow" : 220,
    "Aman" : 85,
    "Gunja" : 210   
}
 n = input("Enter Key To Show Its Marks : ")

 for i in student.keys():
   print(student[n])
   break
   
except KeyError:
    print("Key Not Found")
except SyntaxError:
  print("Syntax")
else:
  print("Key Found")
finally:
  print("Done")'''


'''age = int(input("Enter Your Age Please : "))
print(age)
if age<0:
    raise Exception("Invalid Age , Try Something Else")'''
'''def TooSmallError():
    print("Its Very Small Error")
def TooLarger():
    print("Its Very Bigger Error")

a = int(input("Enter Any Number : "))
print(a)
if a<10:
    raise TooSmallError()
else:
    raise TooLarger()'''
'''class WeakPasswordError(Exception):
    pass

n = input("Enter A Strong Password : ")
i = len(n)
if i<8:
    raise WeakPasswordError("Your PassWord Is Less Than 8 Characters ")
if not any(char.isdigit() for char in n):
    raise WeakPasswordError("There Arnt Digits in ur Password,its weak")
else:
    print("Cool")
print("Done")'''
'''
print("Welcome To Mini Calculator")
a = int(input("Enter A : "))
b = int(input("Enter B : "))
n = input("Enter a Sign To Operate : ")
op = {
    "+" : lambda a,b:a+b,
    "-" : lambda a,b : a-b,
    "*" : lambda a,b : a*b,
    "/" : lambda a,b : a/b
}
op(a,b,n)

 '''
'''a = int(input("Enter A : "))
b = int(input("Enter B : "))
x = lambda a,b:a+b
print(x(a,b))'''
'''a = int(input("Enter A : "))
x = lambda a:a**2
print(f"Square Of {a} Is : ",x(a))'''

'''a = input("Enter A String To Print Its Last Character : ")
x = lambda a:a[-1]
print(f"Last Word Of {a} Is : ",x(a))'''

'''class MeowError(Exception):
 pass

a = int(input("Enter A Number To Check Its Even Or Not : "))

if not a.is_integer():
 raise MeowError("Its An String")

x = lambda a : "Zero" if a==0  else ("Odd" if a%2!=0 else ("Even" if a%2==0 else "Invalid"))
print(x(a))

print("Done")'''


'''try:
 a = list(map(int,input("Enter Elements : ").split()))
 x = list(map(lambda a : a**3,a))
 print(x)
except ValueError:
 print("Its A Char Instead Of Digit")

print("Meow")
'''
'''a = list(map(int,input("Enter Elements : ").split()))
x = list(filter(lambda a : a%2==0,a))
print(x)'''



# def greet():
#     print("Hello")
# greet()

# def display():
#     print("Hello")
# display()

# def add(a,b):
#     print("Sum : ",a+b)
# add(6,9)

# def display(name):
#     print(name + " Ok")
# display("Mayank")
# display("Aman")
'''*args To take multiple input into a variable funtion * means all values passed in funtion will perform the operation
its an tuple , stores data as a tuple , we can fetch aceess the value'''
# def show(*args):
#     print("Value Is : ",count[2])
# show(1,2,3,4,5,6)

# def display(one,two,three):
# #     print("value is : ",three)
# # display(one=1,two=2,three=3)
"""**kwargs means its an dictionary type of ds which containes key as well as value"""
# def display(**kwargs):
#     print("Value Is : ",kwargs.values())
# display(one=1,two=2,three=3)

# def display(food):
#     for i in food:
#         print(i,end = " ")

# fruits =  ["Mango","Apple","Meow"]
# display(fruits)

# def multiply(a,b):
#     return a*b

# print(multiply(5,6))

# def square(a):
#     return a**2
# print("Square Is :",square(5))

# wap to check number is even or not
# def checkOddEven(a):
#     #num = int(input("Enter A Number : "))
#     if a%2==0:
#         print("Its Even ")
#     elif a%2!=0:
#         print("Its Odd")
#     elif a==0:
#         print("Its Zero")
#     else:
#         print("Enter Valid Choice")
# checkOddEven(10)

"""Factorial of a number """
# def factorial(a):
#     if a==0 or a==1:
#         return 1
#     else:
#         return a*factorial(a-1)
# print(factorial(3))
"""Simple Interest"""
# def SI(p,r,t):
#     return (p*r*t)/100

# print(SI(1000,5,2))
# def largestOfThree(a,b,c):
#     print(max(a,b,c))
# largestOfThree(100,2,80)

"""count vowels in string"""
# def countVowels(a):
#     count = 0
#     for i in a:
#         if i.lower() in ['a','e','i','o','u']:
#             count+=1
#     print("Total Vowels In Your String Is : ",count)
# countVowels("The Name Is")
'''a = 1234 , sum = 1,sum='''
# a=1234
# # a= a/10
# # a = a//10
# sum = 0
# while a>0:
#  a = a%10
#  sum+=a
# print(sum)


# def sumOfDigit(a):
#     sum=0
#     for i in range(len(a)):
#         a = a%10
#         sum+=a
#     print(sum)
# sumOfDigit(1245)

# def sumOfDigits(a):
#     sum = 0
#     while a!=0:
#         a = a//10
#         sum+=a
#     print(sum)
# sumOfDigits(1234)


# name_l = []
# score_l = []
# for i in range(4):
#         name = input("Enter Name : ")
#         score = float(input("Enter Marks : "))
#         name_l.append(name)
#         score_l.append(score)
# score_l.sort()
# name_l.sort()
# for scores in score_l:
#         print(score_l[len(score_l)-1])
# print(name_l,score_l)

# a = list(map(int , input("Enter Positive Numbers : ").split()))
# print("List Is : ",a)
# unique = []
# for num in a:
#     if num not in unique:
#         unique.append(num)
# print(unique)

#[15,14,2,18,15,12,98,56,14]
# a = list(map(int,input("Enter Elements : ").split()))
# print(a)
# count = 0
# for num in range(len(a)):
#     if a[num]==a[num+1]:
#         count+=1
# print(f"{num} occured {count} Times ")

# l = list(map(int,input("Enter Elements : ").split()))
# for i in range(len(l)):
#     count=1
#     if i<len(l)-1:
#         for j in range(i+1,len(l)):
#             if l[i]==l[j]:
#                 count+=1
#             if count>=2:
#                 print(f"{l[i]} comes {count} times")

# a = list(map(int,input("Enter Elements : ").split()))
# print("Original List : ", a)

# rev = a[::-1]
# print("Reversed List : ", rev)

# sum_odd = 0
# for num in a:
#     if num % 2 != 0:
#         sum_odd += num

# print("Sum Is : ", sum_odd)






mat  = []
row = int(input("Number Of Rows : "))
col = int(input("Enter Col : "))

for i in range(row):
    rows = []
    for j in range(col):
        data = int(input(f"Enter {i} and {j} : "))
        rows.append(data)
    mat.append(rows)
print(mat)   #print entire matrix

a = [[1,2,3],[],[4,5,6]]
maxlen = len(a[0])
for row in a:
    if len(row) > maxlen:
        maxlen = len(row)
        
