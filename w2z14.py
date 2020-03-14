while 1:
    try: 
      w = int(input('podaj liczbę do spierwiastkowania: '))
      assert w > 0 
      break
    except AssertionError :  
      print("liczba jest ujemna")

print(w**0.5)