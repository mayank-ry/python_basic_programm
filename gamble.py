import random as rd

lucky_draw = rd.randint(1,10)
account = 1000
while account>100:
    user = input("Continue Y/N : ").upper()
    if user=="Y":
        bet = int(input("Your Bet From 1-10 : "))
        if account<100:
            print("Insufficient Amount")
            print("Account Balance : ",account)
        elif bet==lucky_draw:
            print("You Won")
            account+=900-100
            print("Total Amount : ",account)
        else:
            account-=100
            print("Required Bet Is : ",lucky_draw)
            print("You Lost Buddy")
            print("Total Amount : ",account)
    elif user=="N":
        print("Thank You , Visit Again !!")
        break
    else:
        print("Enter A Valid Choice , BYE BYE")
        