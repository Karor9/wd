class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def naOdwrot(self):
        for ind in range(self.index-1, -1, -1):
            yield self.data[ind]

tak = Wspak("Marek")

wspak = tak.naOdwrot()
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())
