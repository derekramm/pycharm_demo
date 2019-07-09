class Target:
    def target_show(self): pass

class Adaptee:
    def adaptee_show(self): return self.adaptee_show

class Adapter(Target):
    def __init__(self, adaptee): self.__adaptee = adaptee
    def target_show(self):
        print(self.__adaptee.adaptee_show())

if __name__ == '__main__':
    Adapter(Adaptee()).target_show()
