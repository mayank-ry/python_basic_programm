try:
    num = 10
    den = 0
    res = num/den
    print(res)
except ZeroDivisionError:
    print("Cant Be Divided By Zero")
finally:
    print("Chal Chal Chal")
print("Out Of Code Block")