bill = float(input("Enter Total Bill : "))
ppl = int(input("Total Person : "))
each_person = bill//ppl
remain = bill%ppl
print("Bill Per Person : ",each_person)
print("Remaining Amount : ",remain)