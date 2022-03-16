class SuperClass:

    variabila_clasa = 6

    def __init__(self, nume):
        self.name = nume
        self.var1 = 101

    def __str__(self):
        return f'Numele meu este: {self.name}'


class Clasa3:

    variabila_clasa = 5

    def __init__(self, nume):
        self.name = nume
        self.var2 = 201


class SubClass(Clasa3, SuperClass):

    subVar = 2
    supVar = 1
    var2 = 101

    def __init__(self, nume):
        var2 = 102
        super().__init__(nume)              # super().__init__ invoca de la Clasa3, de la stanga la dreapta

        self.var3 = 301

    def prima_metoda(self):
        return 4
    #
    def __str__(self):                  # daca este si in Sub, nu mai acceseaza __str__ din Super
        return f'Nume: {self.name}'


obiect = SubClass('Alexandra')
print(obiect.subVar)
print(obiect.supVar)
print(obiect.variabila_clasa)
print(obiect.var3, obiect.var2)     # valoarea var2 este rescrisa de constructor