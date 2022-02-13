import random


întrebare = input('Vrei sa începi tu jocul? "y/n" ')

lista = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
if întrebare == 'y':
    poziție_jucător = int(input("Zi-mi un număr de la 1 la 9! "))
    while poziție_jucător < 1 or poziție_jucător > 9:
        print("Numar gresit! Alege din nou!")
        poziție_jucător = int(input("Zi-mi un număr de la 1 la 9! "))
    if lista[poziție_jucător - 1] == "-":
        lista[poziție_jucător - 1] = '[X]'

while "-" in lista:

    if lista[4] == "-":
        lista[4] = '[0]'
    elif lista[0] == "-":
        lista[0] = '[0]'
    elif lista[2] == "-":
        lista[2] = '[0]'
    elif lista[6] == "-":
        lista[6] = '[0]'
    elif lista[8] == "-":
        lista[8] = '[0]'
    else:
        rămas = [1, 3, 5, 7]
        computer = random.choice(rămas)
        while computer not in rămas:
            lista[computer] = '[0]'
            break

    print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{}".
          format(lista[0], lista[1], lista[2], lista[3],
                 lista[4], lista[5], lista[6], lista[7], lista[8]))

    if lista[0] == lista[1] == lista[2] != "-":
        if lista[0] == '[X]':
            print('Ai câștigat!')
            break
        else:
            print('Ai pierdut!')
            break
    elif lista[3] == lista[4] == lista[5] != "-":
        if lista[3] == '[X]':
            print('Ai câștigat!')
            break
        else:
            print('Ai pierdut!')
            break
    elif lista[6] == lista[7] == lista[8] != "-":
        if lista[6] == '[X]':
            print('Ai câștigat!')
            break
        else:
            print('Ai pierdut!')
            break
    elif lista[0] == lista[3] == lista[6] != "-":
        if lista[0] == '[X]':
            print('Ai câștigat!')
            break
        else:
            print('Ai pierdut!')
            break
    elif lista[1] == lista[4] == lista[7] != "-":
        if lista[1] == '[X]':
            print('Ai câștigat!')
            break
        else:
            print('Ai pierdut!')
            break
    elif lista[2] == lista[5] == lista[8] != "-":
        if lista[2] == '[X]':
            print('Ai câștigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[0] == lista[4] == lista[8] != "-":
        if lista[0] == '[X]':
            print('Ai câștigat!')
            break
        else:
            print('Ai pierdut!')
            break
    elif lista[2] == lista[4] == lista[6] != "-":
        if lista[2] == '[X]':
            print('Ai câștigat!')
            break
        else:
            print('Ai pierdut!')
            break


    poziție_jucător = int(input("Zi-mi un numar de la 1 la 9! "))
    if lista[poziție_jucător - 1] == "-":
        lista[poziție_jucător - 1] = '[X]'
