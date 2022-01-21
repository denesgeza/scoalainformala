# TEMA 2.
# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
def suma_tuturor(n):
    # 1. suma tuturor numerelor de la [0, n]
    if n == 0:
        return 0
    return n + suma_tuturor(n - 1)


# Verificare
print(80 * '-')
for i in range(15):
    print(f"Suma numerelor de la 0 la {i}: ", suma_tuturor(i))
print(80 * '-')


# 2. suma numerelor pare de la [0, n]
def suma_numere_pare(n):
    if n <= 1:
        return 0
    if n == 2:
        return n
    if n == 3:
        return n - 1
    if n % 2 == 0:
        return n + suma_numere_pare(n - 2)
    else:
        return n - 1 + suma_numere_pare(n - 2)


# Verificare
for i in range(15):
    print(f"Suma numerelor pare de la 0 la {i}: ", suma_numere_pare(i))
print(80 * '-')


# 3. suma numerelor impare de la [0. n]
def suma_numere_impare(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n % 2 != 0:
        return n + suma_numere_impare(n - 2)
    else:
        return n - 1 + suma_numere_impare(n - 2)


# Verificare
for i in range(15):
    print(f"Suma numerelor impare de la 0 la {i}: ", suma_numere_impare(i))
print(80 * '-')
