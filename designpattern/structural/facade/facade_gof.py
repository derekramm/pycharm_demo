class ProductA:
    def show_a(self): print(self.show_a)

class ProductB:
    def show_b(self): print(self.show_b)

class Facade:
    def __init__(self):
        self.pa = ProductA()
        self.pb = ProductB()
    def show(self):
        self.pa.show_a()
        self.pb.show_b()

if __name__ == '__main__':
    Facade().show()
