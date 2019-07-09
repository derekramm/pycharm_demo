class Interpreter:
    def interpret(self, context): pass

class InterpreterA(Interpreter):
    def interpret(self, context): return str(context)
class InterpreterB(Interpreter):
    def interpret(self, context): return eval(context)

if __name__ == '__main__':
    ita, itb = InterpreterA(), InterpreterB()
    print(ita.interpret(999))
    print(itb.interpret('[1,2,3]'))
