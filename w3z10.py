
def zakupy(** lista):
    return sum(int(values) for values in lista.values())


print(zakupy(kapusta="4", marchew="10", ser="2"))