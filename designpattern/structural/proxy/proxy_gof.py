from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def show(self): raise NotImplemented

class Target(Subject):
    def show(self): print(self.show)

class Proxy(Subject):
    def __init__(self): self.target = Target()
    def show(self): self.target.show()

if __name__ == '__main__':
    Proxy().show()