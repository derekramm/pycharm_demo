class Aggregate:
    def __init__(self): self.items = []
    def get_iterator(self): return Iterator(self)
class Iterator:
    def __init__(self, agg):
        self.aggregate = agg
        self.index = 0
    def isdone(self): return self.index >= len(self.aggregate.items)
    def get_current(self): return self.aggregate.items[self.index]
    def next(self): self.index += 1

if __name__ == '__main__':
    aggregate = Aggregate()
    aggregate.items.extend('abcde')
    iterator = aggregate.get_iterator()
    while not iterator.isdone():
        print(iterator.get_current())
        iterator.next()
