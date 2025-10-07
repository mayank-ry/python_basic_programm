days = int(input("Enter days Late : "))
if days>=0 and days<=5:
    print("Your Fine Is (5rs/day) : ",5*days)
elif days>=6 and days<10:
    print("Your Fine Is (10rs/day) : ",days*10)
elif days>=10 and days<=29:
    print("Your Fine Is (20rs/day) : ",days*20)
elif days>=30:
    print("Your Membership has been cancelled")
else:
    print("Enter Valid Days")
