import random


def cine_începe():
    """Return True daca începe jucătorul"""
    întrebare = input('Vrei sa începi tu jocul? "y/n" ')
    if întrebare == 'y':
        return True
    else:
        return False


def alegere_jucător(lista):
    poziție_jucător = int(input("Zi-mi un număr de la 1 la 9! "))
    while poziție_jucător < 1 or poziție_jucător > 9:
        print("Număr greșit! Alege din nou!")
        poziție_jucător = int(input("Zi-mi un număr de la 1 la 9! "))
    while lista[poziție_jucător - 1] != "-":
        print("Poziție ocupata! Alege din nou!")
        poziție_jucător = int(input("Zi-mi un număr de la 1 la 9! "))
    else:
        lista[poziție_jucător - 1] = '[X]'


def alegere_calculator(lista):
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
        while lista[computer - 1] == '[X]':
            computer = random.choice(rămas)


def verificare_câștigător(lista):
    result = ''
    if lista[0] == lista[1] == lista[2] != "-":
        if lista[0] == '[X]' or lista[0]:
            result = 'Ai câștigat!'
        else:
            result = 'Ai pierdut!'
    elif lista[3] == lista[4] == lista[5] != "-":
        if lista[3] == '[X]':
            result = 'Ai câștigat!'
        else:
            result = 'Ai pierdut!'
    elif lista[6] == lista[7] == lista[8] != "-":
        if lista[6] == '[X]':
            result = 'Ai câștigat!'
        else:
            result = 'Ai pierdut!'
    elif lista[0] == lista[3] == lista[6] != "-":
        if lista[0] == '[X]':
            result = 'Ai câștigat!'
        else:
            result = 'Ai pierdut!'
    elif lista[1] == lista[4] == lista[7] != "-":
        if lista[1] == '[X]':
            result = 'Ai câștigat!'
        else:
            result = 'Ai pierdut!'
    elif lista[2] == lista[5] == lista[8] != "-":
        if lista[2] == '[X]':
            result = 'Ai câștigat!'
        else:
            result = 'Ai pierdut!'
    elif lista[0] == lista[4] == lista[8] != "-":
        if lista[0] == '[X]':
            result = 'Ai câștigat!'
        else:
            result = 'Ai pierdut!'
    elif lista[2] == lista[4] == lista[6] != "-":
        if lista[2] == '[X]':
            result = 'Ai câștigat!'
        else:
            result = 'Ai pierdut!'
    if result == 'Ai câștigat!':
        print('Ai câștigat!')
        return True
    elif result == 'Ai pierdut!':
        print('Ai pierdut!')
        return True
    else:
        return False


def joc():
    lista = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    if cine_începe():
        while not verificare_câștigător(lista):
            alegere_jucător(lista)
            print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{} \n".
                  format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8]))
            alegere_calculator(lista)
            print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{} \n".
                  format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8]))
    else:
        while not verificare_câștigător(lista):
            alegere_calculator(lista)
            print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{} \n".
                  format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8]))
            alegere_jucător(lista)
            print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{} \n".
                  format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8]))


if __name__ == '__main__':
    joc()
