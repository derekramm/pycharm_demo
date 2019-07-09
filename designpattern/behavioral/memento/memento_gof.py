class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
    def save(self): return Memento(self.price, self.count)
    def load(self, memento):
        self.price = memento.price
        self.count = memento.count
class Memento:
    def __init__(self, price, count):
        self.price = price
        self.count = count
class Director:
    def __init__(self): self.mementos = dict()
    def add(self, key, mem): self.mementos[key] = mem
    def remove(self, key): del self.mementos[key]

if __name__ == '__main__':
    p = Product('python', 10, 100)
    d = Director()
    d.add(1, p.save())
    p.price, p.count = 99, 999
    print(p.__dict__)
    p.load(d.mementos[1])
    print(p.__dict__)
