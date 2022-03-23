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

from datetime import datetime


class CNP:

    def __init__(self, cnp):
        self.cnp = cnp

    def lungime(self):
        return len(self.cnp) != 13 or not self.cnp.isdigit()

    def sex(self):
        return int(self.cnp[0]) in range(1, 10)

    def data_nașterii(self):
        try:
            datetime.strptime(self.cnp[1:7], "%y%m%d")
            return True
        except ValueError:
            return False

    def judet(self):
        return self.cnp[7:9] in ["%02d" % i for i in range(1, 47)] or int(self.cnp[7:9]) in [51, 52]

    def nnn(self):
        return self.cnp[9:12] in ["%03d" % i for i in range(1, 1000)]

    def cifra_de_control(self):
        n = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
        suma = 0
        for i, j in zip(self.cnp[:12], n):
            suma += int(i) * j
        a = suma % 11
        c = a
        if a == 10:
            c = 1
        return int(self.cnp[12]) == c

    def validare(self):
        if not self.cnp.isdigit():
            return "\nAti introdus un CNP invalid."
        elif self.sex() and self.data_nașterii() and self.judet() and self.nnn() and self.cifra_de_control():
            return "\nAti introdus un CNP valid."
        return "\nAti introdus un CNP invalid."


cnp_1 = CNP("19304120605")
print(cnp_1.validare())