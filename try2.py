#syntaxt error , value error , attribute error, zerodivisionError , IO error , Import Error , type error , key error
#raise a customised error
try:
    x = int(input("Enter Less Than 100  :  "))
    if x>100:
        raise ValueError(x)
except ValueError:
    print("Out Of Range Value")
else:
    print("COngrats ! ")
finally:
    print("Out Of Finaallllllyy")

