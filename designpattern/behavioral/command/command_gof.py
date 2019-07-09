class Receiver:
    def show_a(self): print(self.show_a)
    def show_b(self): print(self.show_b)

class Command:
    def __init__(self, r): self.receiver = r
    def show(self): pass
class CommandA(Command):
    def show(self): self.receiver.show_a()
class CommandB(Command):
    def show(self): self.receiver.show_b()

class Invoker:
    def __init__(self): self.__commands = []
    def add(self, c): self.__commands.append(c)
    def remove(self, c): self.__commands.remove(c)
    def notify(self):
        for c in self.__commands: c.show()

if __name__ == '__main__':
    receiver = Receiver()
    invoker = Invoker()
    invoker.add(CommandA(receiver))
    invoker.add(CommandB(receiver))
    invoker.notify()
