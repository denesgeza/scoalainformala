

def your_function(nume: str) -> str:
    print('Hello', nume)
    return nume


# name = input('Numele meu este: ')
# your_function(name)

import datetime as dt


def verifica_data(date):
    try:
        dt.datetime.strptime(date, '%y%m%d')
        print('Data corecta!')
        return True
    except ValueError:
        print('Data nu este corecta!')
        return False


data = '220229'
verifica_data(data)


a = '1980101142608'

lista = list(a)

print(lista)


def my_function(a: str, b: str, c: str) -> (str, str, str):
    # returneaza un tuplu
    return a, b, c


valoare_a = my_function(a='1', b='2', c='3')[0]
print(valoare_a)


def my_other_function(n: int) -> bool:
    if n % 2 == 0:
        return True
    return False


nr = input('Introdu un nr: ')
if my_other_function(int(nr)) is True:
    print('Nr par')
elif my_other_function(int(nr)) is False:
    print('Nr nu este divizibil!')


try:
    valoare = int(input('Prima cifra din CNP'))
    impartire = 1/valoare
except ValueError:
    print("Ai introdus o litera in loc de cifra")
except Exception as e:
    # trateaza absolut toate exceptiile
    print("Exceptie la impartire", e)

# as e ca sa putem vedea care a fost expectia