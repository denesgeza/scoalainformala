# Reguli

word = 'onomatopee'

lista_cuvant = []
for iterator in word:
    lista_cuvant.append('_')
    if iterator == word[0] or iterator == word[-1]:
        lista_cuvant[-1]  = iterator

numar_incercari = 1
lista_litere_incercate = []
while numar_incercari <= 7:
    litera = input("Alege o litera: ")
    if litera in word:
        for index, valoare in enumerate(word):
            if valoare == litera:
                lista_cuvant[index] = litera
    else:
        lista_litere_incercate.append(litera)
        print(f'Litera nu exista, deja ai incercat urmatoarele litere {",".join(lista_litere_incercate)}')
        print(f'Mai ai {7 - numar_incercari} incercari')
        if litera not in lista_litere_incercate:
            numar_incercari += 1
    print(' '.join(lista_cuvant))
