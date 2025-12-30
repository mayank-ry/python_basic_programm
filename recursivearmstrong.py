def armstrong(n,c):
    if n==0:
        return 0
    return (n%10)**c + armstrong(n//10,c)
num = input("Enter A Number : ")
n = int(num)
c = len(num)
if armstrong(n,c)==n:
    print("Armstrong Number")
else:
    print("Not An Armstrong")

def armstrong(n, c):
    if n == 0:
        return 0
    return (n % 10) ** c + armstrong(n // 10, c)

