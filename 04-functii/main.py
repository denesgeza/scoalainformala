

def functia_mea(param_1):
    pass


def suma(a: int, b: int, c: int = 0) ->(int, int):
    """

    :param a: Primul parametru
    :type a:
    :param b: Al doilea parametru
    :type b:
    :return: Returneaza suma parametrilor
    :param c: Parametru c
    :type c:
    :rtype:
    """
    return a + b + c, a - b - c

variabila_1 = 1
variabila_2 = 2

total = suma(variabila_1, variabila_2)

print(total)
print(suma(2, 5))