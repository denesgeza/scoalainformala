def decorator(functie):
    def decoreaza(var):
        return functie(var)
    return decoreaza

def functie(var):
    pass


@decorator
def text(sir):
    return sir.upper()


text_p = decorator(text)
# print(text_p('Salut'))


class Dog:

    def __init__(self, nume):
        self.__name = nume

    @property                   # transforma metoda in atribut, doar citește valoarea din atribut
    def name(self):             # numai trebuie chemata metoda
        return self.__name      # se poate chema cu object.name

    @name.setter                # se scrie `atribut . setter`
    def name(self, nume):       # setează valoarea lui __name
        self.__name = nume

    @name.deleter
    def name(self):
        del self.__name

my_dog = Dog(nume='Rex')
print(my_dog.name)

my_dog.name = 'Codita'
print(my_dog.name)

del my_dog.name
# print(my_dog.name)


class Cat:
    legs = 4

    def __init__(self, nume):
        self.__nume = nume

    @property
    def name(self):
        return self.__nume

    @name.setter
    def name(self, nume):
        self.__nume = nume

    @name.deleter
    def name(self):
        del self.__nume

    def change_name(self, nume):
        self.__nume = nume

    def __str__(self):
        return f'{self.__nume}'


cat = Cat("Fluffy")
print(cat.name)
cat.change_name("Milly")
print(cat.name)
print(cat.legs)

from datetime import date

class Persoana:

    def __init__(self, nume, years):
        self.nume = nume
        self.varsta = years

    @classmethod                                    # dependent de constructor
    def varsta_ani(cls, nume, years):
        return cls(nume, date.today().year - years)  # years = 2022 - years

    @staticmethod                               # nu este dependent de constructor
    def stare(age):
        return age > 18


persoana_1 = Persoana('Ion', 21)
print(persoana_1.varsta)

persoana_2 = Persoana.varsta_ani('Maria', 20)
print(persoana_2.varsta)
print(Persoana.stare(16))