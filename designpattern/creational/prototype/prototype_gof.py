from copy import copy, deepcopy

class Prototype:
    def __init__(self, val, ref):
        self.val = val
        self.ref = ref
    def clone(self): return copy(self)
    def deepclone(self): return deepcopy(self)

if __name__ == '__main__':
    p = Prototype('derek', [0])
    p1, p2 = p.clone(), p.deepclone()
    p.val, p.ref[0] = 'domkn', 18
    print(p.__dict__)
    print(p1.__dict__)
    print(p2.__dict__)
