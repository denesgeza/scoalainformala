# TODO

# declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișează lista inițială ordonată ascendent(lista inițială trebuie păstrată în aceeași formă)
sorted_list = my_list.copy()
sorted_list.sort()

print(80 * '-')
print("Lista originala: ", my_list)
print(80 * '-')
print("Lista sortata: ", sorted_list)
# afișează lista inițială ordonată descendent(lista inițială trebuie păstrată în aceeași formă)
reverse_sorted_list = my_list.copy()
reverse_sorted_list.sort(reverse=True)
print("Lista sortata descendent: ", reverse_sorted_list)

# afișează o listă ce conține numerele pare din lista ordonată(folosind slice)
numere_pare = sorted_list[1::2]
print("Lista de numere pare: ", numere_pare)

# afișează o listă ce conține numerele impare din lista ordonată(folosind slice)
numere_impare = sorted_list[::2]
print("Lista de numere impare: ", numere_impare)

# afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).
multiple_3_list = sorted_list[2::3]
print("Lista cu multipli de 3: ", multiple_3_list)
