class ClasaMea:

    gamma = 0               # atribut

    def __init__(self):     # constructor
        self.alpha = 1      # variabila de instanta
        self.__delta = 3    # variabila de instanta privata


obj = ClasaMea()
obj.beta = 2             # variabila de instanta poate exista doar in interiorul obiectului
print(obj.__dict__)
print(obj._ClasaMea__delta)  # acesarea unei instante private


class Star:

    def __init__(self, nume, galaxie):
        self.name = nume
        self.galaxy = galaxie

    def __str__(self):
        return f'{self.name} este in {self.galaxy}'


soare = Star('Soare', 'Calea Lactee')

print(soare)


class Vehicul:                      # parinte
    pass


class VehiculTeren(Vehicul):        # copil
    pass


class VehiculTractare(VehiculTeren):    # copil
    pass

# parintii sunt superclase pentru copii
# copii sunt subclase pentru parinti

# print('Vehicul', 'VehiculTeren', 'VehiculTractare')
# for cls1 in [Vehicul, VehiculTeren, VehiculTractare]:
#     for cls2 in [Vehicul, VehiculTeren, VehiculTractare]:
#         print(issubclass(cls1, cls2), end='\t')
#     print()

vehicul1 = Vehicul()
vehicul_teren = VehiculTeren()
vehicultractare = VehiculTractare()

print(isinstance(vehicul1, Vehicul))
print(vehicul_teren, Vehicul)

class Exemplu:

    def __init__(self, val):
        self.value = val

obiect1 = Exemplu(8)
obiect2 = Exemplu(0)

str1 = "Maria"
str2 = "Maria"

# TODO: intrebare de interviu
print(str1 is str2) # str1 si str2 points to the same instance

