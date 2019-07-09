class Mediator:
    def send(self, colleague, msg): pass
class ConcreteMediator(Mediator):
    def __init__(self):
        self.ca = None
        self.cb = None
    def send(self, colleague, msg):
        if colleague is self.ca:
            self.cb.receive(msg)
        else:
            self.ca.receive(msg)

class Colleague:
    def __init__(self, mediator): self.mediator = mediator
    def send(self, msg): self.mediator.send(self, msg)
    def receive(self, msg): print(self, msg)
class ColleagueA(Colleague): pass
class ColleagueB(Colleague): pass

if __name__ == '__main__':
    m = ConcreteMediator()
    ca = ColleagueA(m)
    cb = ColleagueB(m)
    m.ca, m.cb = ca, cb
    ca.send('message from ca')
    cb.send('message from cb')
