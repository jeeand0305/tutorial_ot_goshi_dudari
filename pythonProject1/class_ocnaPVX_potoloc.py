import turtle

xod={"one_xod":150, "two":"lift"}
p1 = turtle.Pen()
p2 = turtle.Pen()

p1.forward(150)
p2.left(90)
p2.forward(90)



class asortiment_compan_sion:
    def kto_raditel(self):
        print("товары для продажи в магазине")
    pass
class windows(asortiment_compan_sion):

    pass

class natyznoy_potolok(asortiment_compan_sion):
    def __init__(self, price):
        self.my_price = price
    def read_price(self):
        print("Моя цена: %s" % self.my_price)
    def write_price(self, new_price):
        self.my_price= new_price
    def kto_ya(self):
        print("натяжной потолок")
    pass

class zercala(asortiment_compan_sion):
    pass

obj1 = natyznoy_potolok(205.5)
obj1.kto_ya()
obj1.kto_raditel()
obj1.read_price()
obj1.write_price(509.3)
obj1.read_price()

obj2 = natyznoy_potolok(33.56)
obj2.read_price()


