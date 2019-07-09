class Product: pass
class ProductA(Product): pass
class ProductB(Product): pass

class SimpleFactory:
    @staticmethod
    def get_product(product_name):
        products = dict(a=ProductA, b=ProductB)
        return products[product_name]()

if __name__ == '__main__':
    pa = SimpleFactory.get_product('a')
    pb = SimpleFactory.get_product('b')
    print(pa)
    print(pb)
