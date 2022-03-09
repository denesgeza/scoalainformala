# 2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana cand lista devine goala. (1 punct)
#


def sort_list(lista):

    while len(lista) != 0:
        print(lista[2::3])
        del lista[2::3]
        if len(lista) < 3:
            break
    return 'Gata'



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = sort_list(lista)
print(new_list)
