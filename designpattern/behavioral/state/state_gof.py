class Context:
    def __init__(self, data, state):
        self.data = data
        self.state = state
    def request(self):
        self.state.handle(self)
class State:
    def handle(self, context): pass
class StateA(State):
    def handle(self, context):
        if isinstance(context.data, (int, float, complex)):
            print(self, type(context.data))
        else:
            context.state = StateB()
            context.request()
class StateB(State):
    def handle(self, context):
        if isinstance(context.data, str):
            print(self, type(context.data))
        else:
            context.state = StateC()
            context.request()
class StateC(State):
    def handle(self, context):
        print(self, type(context.data))

if __name__ == '__main__':
    Context(12, StateA()).request()
    Context('python', StateA()).request()
    Context([1, 2, 3], StateA()).request()
