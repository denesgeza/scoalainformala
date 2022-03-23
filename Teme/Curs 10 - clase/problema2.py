class Prajituri:

    nr_prajituri = []

    def __init__(self, name, price=10, weight=500):
        self.name = name
        self.price = price
        self.weight = weight

        self.nr_prajituri.append({
            'type': self.name,
            'price': self.price,
            'weight': self.weight
        })

    @staticmethod
    def cookies_by_weight():
        nr_praji = Prajituri.nr_prajituri
        sortedlist = sorted(nr_praji, key=lambda d: d['weight'], reverse=True)
        return sortedlist

    @staticmethod
    def cookies_by_prices():
        nr_praji = Prajituri.nr_prajituri
        sortedlist = sorted(nr_praji, key=lambda d: d['price'], reverse=True)
        return sortedlist


class Tort(Prajituri):

    def __init__(self, name, etajat=False, glazura='chocolate'):
        super().__init__(name)
        self.etajat = False
        self.glazura = 'chocolate'

    def __str__(self):
        return f'Etajare: {self.etajat}, Glazura: {self.glazura}'

    @property
    def glazurat(self):
        return self.glazura

    @glazurat.setter
    def glazurat(self, glazura):
        self.glazura = glazura

    @glazurat.deleter
    def glazurat(self):
        del self.glazura

    @property
    def etajat(self):
        return self.glazura

    @etajat.setter
    def etajat(self, glazura):
        self.glazura = glazura

    @etajat.deleter
    def etajat(self):
        del self.glazura


class Fursec(Prajituri):
    pass                                            # functioneaza si fara init, mosteneste tot
    # def __init__(self, name, price, weight):
    #     super().__init__(name, price, weight)


tort_1 = Tort('Tort choco', True, 'choco')
tort_2 = Tort('Ceva tort', False, 'ceva')
tort_3 = Tort('Alt tort', True, 'altceva')


fursec_1 = Fursec('Fursec1', 10, 200)
fursec_2 = Fursec('Fursec2', 5, 100)

# print(Prajituri.cookies_by_weight())
# print(Prajituri.nr_prajituri)
print(Fursec.nr_prajituri)
