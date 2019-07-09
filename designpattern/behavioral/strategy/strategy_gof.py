class Func:
    def show(self): pass
class FuncA(Func):
    def show(self): return self.show
class FuncB(Func):
    def show(self): return self.show
class Product:
    def __init__(self, func):
        self.func = func
    def request(self):
        print(self, self.func.show())
if __name__ == '__main__':
    p = Product(FuncA())
    p.request()
    p.func = FuncB()
    p.request()
