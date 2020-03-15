slownik = {
"ziemniaki":"kg","sałata":"szt","mąka":"kg","Zupka chińska":"szt"}

slownik2 = {key:value for key, value in slownik.items() if value=="szt"}


print(slownik2.items())