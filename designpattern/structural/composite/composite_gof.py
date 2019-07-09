class Component:
    def __init__(self, name): self.name = name
    def show(self, level): print('-' * level + self.name)

class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.components = []
    def add(self, c): self.components.append(c)
    def remove(self, c): self.components.remove(c)
    def show(self, level):
        super().show(level)
        for c in self.components:
            c.show(level + 1)
class Leaf(Component): pass

if __name__ == '__main__':
    root = Composite('root')
    node_a = Composite('a')
    node_b = Composite('b')
    node_1 = Leaf('1')
    node_2 = Leaf('2')
    root.add(node_a)
    root.add(node_b)
    node_a.add(node_1)
    node_a.add(node_2)
    node_b.add(node_1)
    node_b.add(node_2)
    root.show(1)
