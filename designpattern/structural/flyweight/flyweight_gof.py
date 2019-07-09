class Flyweight:
    def show(self, x, y): print(self, x, y)
class SharedFlyweightA(Flyweight): pass
class SharedFlyweightB(Flyweight): pass
class UnSharedFlyweight(Flyweight): pass

class FlyweightFactory:
    flyweights = dict(a=SharedFlyweightA(), b=SharedFlyweightB())
    @classmethod
    def get_flyweight(cls, flyweight_name):
        if flyweight_name in cls.flyweights:
            return cls.flyweights[flyweight_name]
        else:
            return UnSharedFlyweight()

if __name__ == '__main__':
    fa1 = FlyweightFactory.get_flyweight('a')
    fa2 = FlyweightFactory.get_flyweight('b')
    fa1.show(1, 1)
    fa1.show(1, 2)
    fc1 = FlyweightFactory.get_flyweight('c')
    fc2 = FlyweightFactory.get_flyweight('c')
    fc1.show(3, 1)
    fc2.show(3, 2)
