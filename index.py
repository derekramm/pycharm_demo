class OrderLine(object):

    def __init__(self, price, count, total):
        self._price = price
        self._count = count
        self._total = total

    def get_total(self): return self._total

class Order(object):
    def __init__(self, order_total):
        self.__order_lines = []

    def add(self, order_line):
        self.__order_lines.append(order_line)

    def remove(self, order_line):
        self.__order_lines.remove(order_line)
