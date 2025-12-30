#wap to implement a function which check given number is armstrong or not
def armstrong(n):
    temp = n
    total = 0
    count = 0
    while n>0:
        count+=1
        n=n//10
    n =temp
    while n>0:
        r = n%10
        total += (r**count)
        n = n//10
    if total==temp:
        print(f"{temp} Is Armstrong")
    else:
        print(f"Its Not A Armstrong")
armstrong()