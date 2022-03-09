# 1. Realizati o functie care sa inlocuiasca textul din variabila string aflat
# intre valorile “start” si “end” cu textul din “text”.
# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be
# introduced."
# # [start, end, text]

# Textul rezultat este: 
# The Conquistator must meet King on top of Palace battlements to be introduced.
# Numaratoarea de start si end incepe cu indexul 1. Se pot introduce de la
# tastatura alte valori pentru index si text, cat si un numar mai mare de liste.
# Optimizati codul.

string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]


def function_2(patch, string):
    text = string
    for i in patch:
        text_mod = text.replace(string[i[0] - 1:i[1]], i[2])
        text = text_mod
    return text


print(function_2(patches, string))

lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']

# 1. Sortati lista dupa nume
lista_nume_sorted = sorted(lista_nume)
print(lista_nume_sorted)

# 2. Determinati numarul de aparitii al fiecarui nume
# name_count = [{name: lista_nume.count(name)} for i, name in enumerate(lista_nume)]
# print(name_count)


def duplicat(lista):
    return list(dict.fromkeys(lista))

print(duplicat(lista_nume))


# 3. Listati numele care apare de cele mai multe ori in lista initiala.
counts = dict()
for i in lista_nume:
    counts[i] = counts.get(i, 0) + 1
print(max(counts, key=counts.get))

# 4. Listati numele care apare de cele mai putine ori in lista initiala.
print(min(counts, key=counts.get))


def palindrom(string):
    if string == string[::-1]:
        return True
    return False

def invers(string):
    return string[::-1]

print(invers("Astazi"))

from itertools import permutations


def functie(string):
    return [''.join(p) for p in permutations(string)]


print(functie("2635"))


def generatePermutation(string, start, end):
    current = 0
    # Prints the permutations
    if (start == end - 1):
        print(string)
    else:
        for current in range(start, end):
            # Swapping the string by fixing a character
            x = list(string)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

            # Recursively calling function generatePermutation() for rest of the characters
            generatePermutation("".join(x), start + 1, end)
            # Swapping the string by fixing a character
            temp = x[start]
            x[start] = x[current]
            x[current] = temp


str = "AB"
n = len(str)
print("All the permutations of the string are: ")
generatePermutation(str, 0, n)
