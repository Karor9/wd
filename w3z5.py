def relacja(a1, a2):
    if a1==a2:
        print("Proste równoległe")
    elif a1*a2==-1:
        print("Proste prostopadłe")
    else:
        print("Brak relacji")

print(relacja(1, 5))
print(relacja(-5, 5))
print(relacja(1, 1))