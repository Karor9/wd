
import math as m
n=0
while n < 3 or n >9:
    n=int(input("Wybierz liczbę między 3 a 9"))
g = m.ceil(n/2+1)
d = m.floor(n/2) 

for i in range (1,g):
    for j in range (g-i):
        print(' ', end = '')
    for j in range (i*2 -1):
        print('o', end = '')
    print('')
for i in range (d, -1, -1):
    for j in range (g - i):  
        print(' ', end = '') 
    for j in range (i*2-1):
        print('o', end = '')
    print('')

