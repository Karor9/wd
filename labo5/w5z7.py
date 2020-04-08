class Parzyste:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.ln = len(data)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.ln:
            raise StopIteration
        self.index = self.index + 2
        return self.data[self.index-2]

tak = Parzyste("123456789")
print(tak.__iter__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
