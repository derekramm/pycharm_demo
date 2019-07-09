class Visitor:
    def visit_element_a(self, ea): pass
    def visit_element_b(self, eb): pass
class Visitor_1:
    def visit_element_a(self, ea): print(self, ea)
    def visit_element_b(self, eb): print(self, eb)
class Visitor_2:
    def visit_element_a(self, ea): print(self, ea)
    def visit_element_b(self, eb): print(self, eb)

class Element:
    def accept(self, visitor): pass
class ElementA:
    def accept(self, visitor): visitor.visit_element_a(self)
class ElementB:
    def accept(self, visitor): visitor.visit_element_b(self)

class Director:
    def __init__(self):
        self.elements = [ElementA(), ElementB()]
    def visit(self, visitor):
        for element in self.elements:
            element.accept(visitor)

if __name__ == '__main__':
    d = Director()
    d.visit(Visitor_1())
    d.visit(Visitor_2())
