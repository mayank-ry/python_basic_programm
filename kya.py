import os
os.system("cls")
# def power(x,y):
#     return x**y
# a = int(input("Enter A : "))
# b = int(input("Enter B : "))
# c = power(a,b)
# print("A To The Power Of B Is : ",c)

# def meow():
#     print("Hello World")
# meow()

# def add(a,b):
#     print("Sum Is : ",a+b)
# add(5,8)

# def get_number():
#     return 10

# result = get_number()
# print(result)
"""wap to implement function which return prime number from 1 to n"""

# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")

#.Write a Python program to create a class Person with
#  attributes name and age. Create a child class Employee that 
# adds employee ID and salary.
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# class Employee(Person):
#     def __init__(self,name,age,EID,salary):
#         super().__init__(name,age)
#         self.EID = EID
#         self.salary = salary
        
#     def details(self):
#         print(f"{self.name} : {self.EID} \nEarns {self.salary} at The Age of {self.age}")

# E1 = Employee("Mayank" , 18,"W101",18520)
# E1.details()

# num = int(input("Enter A Number : "))
# sqr = 0
# while sqr!=1:
#     a = num%10
#     num = num//10
#     print("a = ",a)
#     print("num = ",num)
#     sqr = (a**2) + (num**2)
#     print("Sum Of Their Square : ",sqr)
#     num = sqr
#     # a = num%10
#     # num = num//10
#     # print("num = ",num)
#     # print("a = ",a)
#     # sqr = (a**2) + (num**2)
#     # print("Sum Of Their Square : ",sqr)
# else:
#     print("Bye Bye")



# num = int(input("Enter a number: "))

# while num != 1:
#     sum_sq = 0
#     temp = num

#     while temp > 0:
#         digit = temp % 10
#         sum_sq += digit ** 2
#         temp //= 10

#     print("Sum of squares : ", sum_sq)
#     num = sum_sq

# print("Bye Bye")


""" wap to display all words of a list which starts with vowels """

# list1 = ['Aman','Chal','Murtaja','Amarkantak','Usman','Chandan']
# list2 = []
# list3 = []
# meow = 'AEIOUaeiou'
# for words in list1:
#     if words[0] in meow:
#         list2.append(words)
#     else:
#         list3.append(words)

# print("Words Start With Vowels : ",list2)
# print("Words Not Start With Vowels : ",list3)
            
""" wap to implement a function which  returns prime number from 1 to n """


# 
# list1= []
# n = int(input("Enter A Number : "))
# while n<2:
#     print("Bye Bye")
   
# else:
#     for i in range(1,n+1):
#         if n!=i or n!=1:
#             list1.append(n)
# print(list1)
