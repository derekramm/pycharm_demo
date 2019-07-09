class Component:
    def __init__(self, name): self.name = name
    def show(self): return self.name
class Product(Component): pass
class Decorator(Component):
    def __init__(self, name):
        super().__init__(name)
        self.component = None
class DecoratorA(Decorator):
    def show(self): return f'[{self.component.show()}]'
class DecoratorB(Decorator):
    def show(self): return f'<{self.component.show()}>'

if __name__ == '__main__':
    p = Product('product')
    da = DecoratorA('da')
    db = DecoratorB('db')
    da.component = p
    db.component = da
    print(p.show())
    print(da.show())
    print(db.show())
