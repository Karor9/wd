with open("labo4/zadanie3.txt", "w+") as plik:
    for x in range(1, 5):
        plik.write("To jest linia numer " + str(x) + "\n")


with open("labo4/zadanie3.txt", "r") as pliks:
    for linia in pliks:
        print(linia, end="")        