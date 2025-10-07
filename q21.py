a=input("Enter Word : ")
b=input("Enter Letter to search : ")
c=print(a.find(b))
if b in a:
    print("found")
else:
    print("not found")