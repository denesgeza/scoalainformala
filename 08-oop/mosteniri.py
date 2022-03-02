# 1. Vehicul
# 1.1. Vehicul de apa
# 1.2 Vehicul aer
# 1.3  Vehicul de spatiu
# 1.4 Vehicul terestru
# 1.4.1 Vehicul de teren
# 1.4.2 Vehicu de cursa

#1 este super clasa pt 1.1 - 1.4
# 1.4 este super clasa pt 1.4.1 si 1.4.2
# 1.4.1 si 1.4.2 sunt subclase pt 1.4 si pt 1

# Exemplu

# Max este un caine mare care doarme toata ziua
# obiectul -> Max (substantiv) -> instanta creata din clasa
# clasa -> caine (substantiv) -> clasa
# proprietatea -> marime "mare" (adjectiv)
# activitatea -> "doarme" (verb) -> metoda / functie


# Un Logan verde merge incet.
##############################
# obiect: Logan
# clasa: masina
# proprietate: verde
# activitate: merge

stack = []


def push(val):
    stack.append(val)
    return stack


def pop():
    val = stack[-1]
    del stack[-1]
    return val

# print(push(3))
# print(push(2))
# print(push(1))
#
# print(pop())
# print(pop())
# print(pop())

# cu `__` facem un obiect privat sa nu se poate accesa din exterior


class Stack:

    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def __str__(self):
        return f'{self.__stack_list}'


# obiect_stiva = Stack()
# # print(obiect_stiva.__stack_list) # => obiect privat
# obiect_stiva.push(3)
# obiect_stiva.push(2)
# obiect_stiva.push(1)
# print(obiect_stiva)
# obiect_stiva.pop()
# print(obiect_stiva)


class ClasaExemplu:

    def __init__(self, val=1):
        self.first = val
        self.second = 0

    def set_second(self, val=2):
        self.second = val

    def __str__(self):
        return f'{self.first} {self.second}'

obiect_1 = ClasaExemplu()
obiect_2 = ClasaExemplu(2)

# afiseaza proprietatile obiectului
print(obiect_1.__dict__)

# afiseaza proprietatile clasei
print(ClasaExemplu.__dict__)

print(obiect_1)

