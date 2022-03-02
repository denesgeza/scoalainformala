class MyFirstClass:
    pass


my_first_object = MyFirstClass()


class Caine:

    # este declarat la nivel de clasa
    nr_picioare = 4  # atribut

    def __init__(self, name, vaccin, age=3):
        self._nume = name        # proprietati ale obiectului
        # adaugand __ variabila devine protejata, neaccesibila
        self.__varsta = age
        self.__vaccin = vaccin
        # preferabil sa fie initializate inainte de if
        self.stare = 'tanar'
        self.cumpara = 'mancare'
        if self.__varsta == 4:
            self.stare = 'batran'
        else:
            self.cumpara = 'jucarie'

    # Acesta este reprezentarea, se va afisa fara print vezi => 1
    def __str__(self):
        return f'{self._nume} - {self.__varsta} ani'
    
    def change_name(self, name):
        # adaugand _ variabila devine protejata
        self._nume = name


print(Caine.nr_picioare)

cainele_meu = Caine('Skye', 2)
print(cainele_meu._nume)
print(cainele_meu)  # 1. Apare numele din cauza ca __str__ este definit

print(cainele_meu.change_name('Ben'))
print(cainele_meu)

# verifica daca exista atributul respectiv
print(hasattr(Caine, 'nr_picioare'))

# verifica numele clasei
print(type(cainele_meu).__name__)
# print(cainele_meu.varsta)


class Calculator:

    def __init__(self, op1, op2, operation):
        self.operator1 = op1
        self.operator2 = op2
        self.operatie = operation

    def adunare(self):
        return self.operator1 + self.operator2

    def scadere(self):
        return self.operator1 - self.operator2

    def __str__(self):
        if self.operatie == '+':
            return f'{self.adunare()}'
        elif self.operatie == '-':
            return f'{self.scadere()}'


obiect1 = Calculator(3, 2, '+')
print(obiect1.__dict__)
print(obiect1)