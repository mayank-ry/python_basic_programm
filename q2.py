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

'''a = []
for num in range(1,11):
    a.append(num**2)
print(a)'''

#to check number is perfet or not
'''a =int(input("Enter Number To Check Its Perfect Or Not : "))
list_1 = []
for i in range(1,a):
    if a%i==0:
        list_1.append(i)
print(list_1)
sum_list = sum(list_1)
if sum_list==a:
    print(f"Number {a} Is Perfect ")
else:
    print(f"Number {a} Is Not Perfect")'''

#n = 1 exit , n=even f(n) = n/2 , n = odd f(n) = 3*n+1
'''n = int(input("Enter The Number : "))
list_1 = []
print(n)
list_1.append(n)

while(n!=1):
 if n==1:
    break
 elif n%2==0:
    n = n//2
 else:
    n = 3*n+1
 list_1.append(n)
print(list_1)
print(max(list_1))'''

#check seat availability
#user count
#ticket confirmation msg
#book a ticket


'''def book():
    ticket = 100
    user_count = 0

    # Inner function: can access outer variables
    def check():
        print(f"\n--- Ticket Status ---")
        print(f"Remaining Tickets : {ticket}")
        print(f"Total Users       : {user_count}\n")

    while ticket > 0:
        user = int(input("Enter No. Of Tickets You Want To Buy : "))

        if user > 4 or user <= 0:
            print("⚠️ Please Buy Between (1-4) Tickets Only")
        elif user > ticket:
            print(f" Only {ticket} tickets left, cannot buy {user}")
        else:
            ticket -= user
            user_count += 1
            print(f"🎟 Congrats! You Bought {user} Ticket(s)")
            print("🙏 Thank You! Visit Again\n")

        # Option to check after each transaction
        want_check = input("Do you want to check seat status? (y/n): ").lower()
        if want_check == 'y':
            check()

    print("🎉 Tickets Are Sold Out! Thank You All\n")

    # Return the inner function so it can be used outside
    return check


# --- Main Program ---
choice = input("Do You Want To (B)ook Ticket or (C)heck Seat Status? : ").upper()

if choice == 'B':
    check_func = book()  # book returns the 'check' function
    print(" Booking session ended.")
    again = input("Do you want to check the final status? (y/n): ").lower()
    if again == 'y':
        check_func()

elif choice == 'C':
    print("⚠️ You can only check after booking at least once.")
else:
    print(" Enter A Valid Choice (B/C).")'''

#function 2 check

list_1 = []
list_2 = []
a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))
for i in range(1,a+1):
    if a%i==0:
        list_1.append(i)
for j in range (1,b+1):
    if b%j==0:
        list_2.append(j)
print("List_1 Is : ",list_1)
print("List_2 Is : ",list_2)
 
















