# tupluri

lista = [1, 2, 3, 1, 'a']
lista_1 = ['a', 'b', 'c']

lista_total = lista + lista_1
print(lista_total)

tuplu = (1, 2, 3, 1, 'a')
tuplu_1 = (1, 2, 3, 'b')

tuplu_total = tuplu + tuplu_1
print(tuplu_total)

tuplu_nou = (1)
print(type(tuplu_nou))

dictionar = {"cheie": '1',
             1: '1',
             'lista': [1, 2, 3]
             }

print(dictionar['cheie'])


dictionar.update({'cheie': 3})
# daca o cheie exista de doua ori, o printeaza doar pe a 2a
# returneaza valorile
print(dictionar.keys())

# returneaza valorile
print(dictionar.values())

# SETS
# toate elementele sunt unice
setul_meu = {1, 1, 3}
