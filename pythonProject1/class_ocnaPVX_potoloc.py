
    def __init__(self, polotno, baget, vstavka, ugli, trub_sto, lite, dict):
        # можоно воздейстовать на price просто */-+
        self.polotno320 = polotno
        self.baget_po_pirimetru = baget
        self.vstavka=vstavka
        self.count_uglov_pomeshenie =ugli
        self.count_trub_stoyka = trub_sto
        self.count_lite_na_potolke = lite

    def read_price(self):
        print("Моя цена: %s" % self.my_price)
    def write_price(self, new_price):
        # можоно воздейстовать на new_price просто */-+
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


