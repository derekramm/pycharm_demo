class Subject:
    def __init__(self): self.observers = []
    def add(self, o): self.observers.append(o)
    def remove(self, o): self.observers.remove(o)
    def notify(self):
        for o in self.observers:
            o.update()
class Observer:
    def __init__(self, subject):
        self.subject = subject
        self.subject.add(self)
    def update(self): pass
class ObserverA(Observer):
    def update(self): print(self, self.subject)
class ObserverB(Observer):
    def update(self): print(self, self.subject)

if __name__ == '__main__':
    s = Subject()
    oa, ob = ObserverA(s), ObserverB(s)
    s.notify()
