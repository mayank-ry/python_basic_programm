'''my_list = list(map(int , input("Enter Numbers : ").split()))
print(my_list)
user = int(input("Enter Number To Check Its Repetition : "))
user_1 = int(input("Enter For Index : "))
l = []

#a = my_list.count(user)
#print(a)
index = 0
for nums in (my_list):
    if nums == user:
        index+=1
print(index)
print(my_list.index(user_1))
my_list.reverse()
my_list.sort()
print(my_list)'''

#use append , extend and + operator on two list to join them
'''list_1 = list(map(int , input("Enter List 1 : ").split()))
list_2 = list(map(int , input("Enter List 2 : ").split()))
list_1.append(list_2)
print(list_1)
#list_1.extend(list_2)
#print(list_1)
#list_3 = list_1 + list_2
#print(list_3)'''

#check element exist in list or not

'''list_1 = list(map(int , input("Enter Elements : ").split()))
user = int(input("Enter Int To Search : "))
if user in list_1:
    print("Founded")
else:
    print("Not Founded")'''

'''list_1 = []
list_2 = []
user = int(input("Enter Number Of Elements In Both List : "))
n=0
for i in range(user):
    i = int(input(f"Enter Number For I ({n}) : "))
    list_1.append(i)
    n = n+1
m = 0
for j in range(user):
    j = int(input(f"Enter Elements For J ({m}) : "))
    list_2.append(j)
    m=m+1

print("List_1 Is : ",list_1)
print("List_2 Is : ",list_2)

list_1[0],list_1[len(list_1)-1] = list_2[len(list_2)-1],list_2[0]
print("List_1 : ",list_1)
print("List_2 : ",list_2)'''

'''list_1 = []
user = int(input("Enter Number Of Elements : "))
n=0
for i in range(user):
    i = int(input(f"Enter ELement Of Idx ({n}) : "))
    list_1.append(i)
    n+=1
print("List_1 Is : ",list_1)
list_1[0],list_1[len(list_1)-1] = list_1[len(list_1)-1],list_1[0]
print("Updated List_1 : ",list_1)'''

'''main_list = []
odd_list = []
even_list = []
user = int(input("Enter Number Of Elements For Main_List : "))
for num in range(1,user+1):
    main_list.append(num)
print(main_list)
for num in main_list:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("Even List : ",even_list)
print("Odd List : ",odd_list)'''

'''a =list(map(int , input("Enter Numbers : ").split()))
print("Original List : ",a)
print("Reversed List : ",a[::-1])'''

a = []
for num in range(1,11):
    a.append(num**2)
print(a)
