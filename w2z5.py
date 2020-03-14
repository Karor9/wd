a = input()
a = int(a)
b = input()
b = int(b)
c = input()
c = int(c)
if 0 < a <= 10 and (a > b) or (b > c):
    print("a jest z przedziału (0, 10> oraz a jest większe od b lub b jest większe od c")
else:
    print("warunki nie zachodzą")