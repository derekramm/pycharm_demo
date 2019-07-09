class Chain:
    def __init__(self, level):
        self.level = level
        self.next = None
    def handle(self, number):
        if self.level >= number:
            print(self, number)
        elif self.next:
            self.next.handle(number)
        else: pass
class ChainA(Chain): pass
class ChainB(Chain): pass

if __name__ == '__main__':
    ca = ChainA(10)
    cb = ChainB(100)
    ca.next = cb
    ca.handle(10)
    ca.handle(100)
