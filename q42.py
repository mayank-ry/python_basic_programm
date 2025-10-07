import os
os.system("cls")

Price = float(input("Enter Price Of Item : "))
Quantity = int(input("Enter Quantity Of Item : "))


def total_amt():
    return Price*Quantity

print("Your Total Bill : ",total_amt())
