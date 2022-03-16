from itertools import permutations

# Scrie un program care sa afiseze toate combinarile de 2 litere dintre valorile dictionarului de mai jos:

dictionar = {"1": "abc", "2": "s", "3": "o", "4": "n", "5": "lm", "6": "jk", "7": "gi", "8": "def", "9": "abc"}


def permutatii(dictionar):
    values = list(dictionar.values())
    for i in values:
        if len(i) < 2:
            continue
        elif len(i) == 2:
            print([''.join(p) for p in permutations(i)])
        elif len(i) == 3:
            print([''.join(p) for p in permutations(i[:2])] + [''.join(p) for p in permutations(i[1:])] + [''.join(p) for p in permutations(i[0] + i[2])])

    return True


permutatii(dictionar)