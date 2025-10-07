unit = int(input("Enter Electricity Consumed : "))
if unit>=0 and unit<=100:
    print("Your Bill Is (5rs/unit) : ",unit*5)
elif unit>=101 and unit<=200:
    print("Your Bill Is (7rs/unit) : ",unit*7)
elif unit>200:
    print("Your Bill Is (10rs/unit) : ",unit*10)
else:
    print("-------Please Enter Valid Units-------")