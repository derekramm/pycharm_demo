class Func:
    def execute(self): pass
class FuncA(Func):
    def execute(self): return self.execute
class FuncB(Func):
    def execute(self): return self.execute

class Product:
    def __init__(self): self.funcs = dict()
    def add(self, key, func): self.funcs[key] = func
    def remove(self, key): del self.funcs[key]
    def request(self, key): print(self, self.funcs[key].execute())
class ProductA(Product): pass
class ProductB(Product): pass

if __name__ == '__main__':
    pa, pb = ProductA(), ProductB()
    pa.add('a', FuncA())
    pa.add('b', FuncB())
    pb.add('a', FuncA())
    pb.add('b', FuncB())
    pa.request('a')
    pa.request('b')
    pb.request('a')
    pb.request('b')
