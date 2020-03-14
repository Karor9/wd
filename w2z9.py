x = input()
x = int(x)
suma = 0
while x>0:
    suma += x%10
    x = x // 10
print(suma)