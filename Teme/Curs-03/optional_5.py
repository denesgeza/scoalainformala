# Validare CNP

# Se dorește realizarea unui validator de CNP. Mai jos se găsesc regulile.
# Codul numeric personal sau CNP este codul unic al fiecărei persoane născute în România, format din exact 13 cifre.

# Format: S AA LL ZZ JJ NNN C

# S reprezintă sexul și secolul în care s-a născut persoana care posedă acel CNP. Persoanelor de sex masculin le sunt atribuite numerele impare iar persoanelor de sex feminin numerele pare.
# Prima cifră a CNP-ului este: (sex bărbătesc / sex femeiesc)
# 1 / 2 - născuți între 1 ianuarie 1900 și 31 decembrie 1999
# 3 / 4 - născuți între 1 ianuarie 1800 și 31 decembrie 1899
# 5 / 6 - născuți între 1 ianuarie 2000 și 31 decembrie 2099
# 7 / 8 - pentru persoanele străine rezidente în România.
# În plus 9 - pentru persoanele străine.

# AA este un număr format din 2 cifre și reprezintă ultimele 2 cifre din anul nașterii. O persoană născută în anul 1970 va avea la AA 70. (SAA = 170)
# LL este un număr format din 2 cifre și reprezintă luna nașterii persoanei.
# ZZ reprezintă ziua nașterii în format de 2 cifre. Pentru zilele de la 1 la 9 se adaugă 0 înaintea datei. Spre exemplificare, o persoană născută în prima zi a lunii va avea codul 01.
# JJ este un număr format din două cifre și este reprezentat de codul județului sau sectorului în care s-a născut persoana ori în care avea domiciliul sau reședința în momentul acordării C.N.P.
#   De exemplu, pentru Buzău acest număr este 10. Pentru București, codul este un număr din intervalul 41 și 46 și reprezintă sectorul în care s-a născut acea persoană.
#   Codurile județelor sunt în ordinea alfabetică a acestora, cu unele excepții.
# NNN este un număr format din 3 cifre din intervalul 001 - 999. Numerele din acest interval se împart pe județe,
#   birourilor de evidență a populației, astfel încât un anumit număr din acel interval să fie alocat unei singure persoane într-o anumită zi.
# C este cifră de control aflată în relație cu toate celelalte 12 cifre ale CNP-ului.
#   Cifra de control este calculată după cum urmează: fiecare cifră din CNP este înmulțită cu cifra de pe
#   aceeași poziție din numărul 279146358279; rezultatele sunt însumate, iar rezultatul final este împărțit
#   cu rest la 11. Dacă restul este 10, cifra de control este 1, altfel cifra de control este egală cu restul

def verifica_luna(luna):
    """Verifica daca numărul de luni este mai mic sau egal cu 12."""
    if luna > 12:
        return "Luna este greșită!"
    return True


def verifica_an(an):
    """Verifica daca este an bisect si returnează True sau False."""
    # Daca persoana are peste 100 de ani, CNP-ul poate fi greșit!
    if an > 22:
        an_cnp = 1900 + an
    else:
        an_cnp = 2000 + an
    if an_cnp % 4 == 0:
        if an_cnp % 100 == 0:
            if an_cnp % 400 == 0:
                return True
            return False
        return True
    return False


def verifica_ziua(luna, zi, an):
    """Verifica daca este posibila ziua in luna si anul respectiv. \n 
       Returnează True sau False."""
    luna_31_zile = [1, 3, 5, 7, 8, 10, 12]
    luna_30_zile = [4, 6, 9, 11]
    # daca e Februarie
    if luna == 2:
        # daca e an bisect
        if verifica_an(an):
            if zi > 29:
                return "Ziua este greșită!"
            return True
        else:
            if zi > 28:
                return "Ziua este greșită!"
            return True
    # daca pică într-o luna cu 30 de zile
    elif luna in luna_30_zile:
        if zi > 30:
            return "Ziua este greșită!"
        return True
    # daca pica într-o luna cu 31 de zile
    elif luna in luna_31_zile:
        if zi > 31:
            return "Ziua este greșită!"
        return True
    return False


def nnn(cnp):
    # https: // stackoverflow.com / questions / 6869999 / fixed - width - number - formatting - python - 3
    if cnp[9:12] in ["%03d" % i for i in range(1, 1000)]:
        return True
    return False


def cifra_de_control(cnp):
    """Verifica dacă cifra de control din CNP este corecta. \n
        Returnează True sau False"""
    control_no = '279146358279'
    index = 0
    suma = 0
    # fiecare cifră din CNP este înmulțită cu cifra de pe aceeași poziție din numărul 279146358279
    for i in control_no:
        suma += int(i) * int(cnp[index])
        # print(int(i), int(cnp[index]), suma)
        index += 1
    # rezultatul final este împărțit cu rest la 11
    rest = suma % 11
    # Dacă restul este 10 => cifra de control este 1
    if rest == 10:
        rest = 1
    # altfel cifra de control este egală cu restul
    if rest == int(cnp[-1]):
        return True
    return "Cifra de control este greșită!"


def verifica_judet(judet):
    """Verifica daca județul din CNP este valid. \n
       Returnează True sau False"""
    if int(judet) in range(47) or int(judet) == 51 or int(judet) == 52:
        return "Județul este greșit"
    return False


def cnp_validator():
    """Verifica daca un cnp introdus este valid."""
    cnp = input("Introduceți cnp-ul: ")
    if cnp.isdigit():
        sex = int(cnp[0])
        an = int(cnp[1:3])
        luna = int(cnp[3:5])
        zi = int(cnp[5:7])
        judet = cnp[7:9]

    # verificăm ca toate caracterele să fie numere
    for char in cnp:
        if not char.isnumeric():
            return "CNP invalid"

    # verificăm ca lungimea sa fie 13, sexul sa nu fie 0 :), dacă data este introdusă corect și cifra de control
    if len(cnp) == 13 and sex != 0 and verifica_luna(int(luna)) and verifica_ziua(zi=zi, luna=luna, an=an) and cifra_de_control(cnp) and verifica_judet(judet) and nnn(cnp):
        return "CNP valid!"
    return "CNP invalid"


if __name__ == '__main__':
    print(cnp_validator())
