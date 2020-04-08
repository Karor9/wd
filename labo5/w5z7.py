class Parzyste:
    index = 0
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.ln = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if Parzyste.index > self.ln:
            raise StopIteration
        Parzyste.index = Parzyste.index + 2
        return self.data[Parzyste.index-2]

tak = Parzyste("123456789")
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
