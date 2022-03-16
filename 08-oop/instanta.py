class Rata:

    ochi = 2

    def __init__(self, inaltime, greutate, gen):
        self.inaltime = inaltime
        self.greutate = greutate
        self.gen = gen

    def merge(self):
        pass

    def macane(self):
        return 'Mac-mac'


rata_1 = Rata(inaltime=10, greutate=3.4, gen='feminin')
rata_2 = Rata(inaltime=20, greutate=4.5, gen='masculin')

print(f'O rata are: {Rata.ochi} ochi')
print(rata_1.macane())