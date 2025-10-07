print("Scientific Calculator")
a=int(input("Enter The Number 1 : "))
b=int(input("Enter The Number 2 : "))
user=input("Choose Sign For Operation :  ")
if(user=="+"):
 print(a+b)
elif(user=="-"):
 print(a-b)
elif(user=="*"):
 print(a*b)
elif(user=="/"):
 print(a/b)
elif(user=="%"):
 print(a%b)
else:
 print("Invalid Choice !!")
