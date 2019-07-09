class Template:
    def show(self):
        print(self, self._get_submethod())
    def _get_submethod(self): pass
class ProductA(Template):
    def _get_submethod(self): return self
class ProductB(Template):
    def _get_submethod(self): return self

if __name__ == '__main__':
    pa, pb = ProductA(), ProductB()
    pa.show()
    pb.show()
