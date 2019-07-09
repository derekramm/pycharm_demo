class Builder:
    def build_part_a(self): pass
    def build_part_b(self): pass

class BuilderA(Builder):
    def build_part_a(self): print(self.build_part_a)
    def build_part_b(self): print(self.build_part_b)
class BuilderB(Builder):
    def build_part_a(self): print(self.build_part_a)
    def build_part_b(self): print(self.build_part_b)

class Director:
    def __init__(self): self.builder = None
    def build(self):
        self.builder.build_part_a()
        self.builder.build_part_b()

if __name__ == '__main__':
    d = Director()
    d.builder = BuilderA()
    d.build()
    d.builder = BuilderB()
    d.build()
