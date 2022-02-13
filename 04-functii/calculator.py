from typing import Tuple


def add(a: int, b: int) -> str:
    return f'{a} + {b} = {a + b}'


def subtract(a: int, b: int) -> str:
    return f' {a} - {b} = {a - b}'


def multiply(a: int, b: int) -> str:
    return f'{a} * {b} = {a * b}'


def divide(a: int, b: int) -> (int, float):
    if b == 0:
        while b == 0:
            b = int(input("Aloca o noua valoare lui b: "))
    if a % b == 0:
        return f'{a} / {b} = {a // b}'
    return f'{a} / {b} = {a / b}'


def operator() -> str:
    op = input('Alege operatorul: ')
    if op not in ['*', '/', '+', '-']:
        while op not in ['*', '/', '+', '-']:
            op = input('Alege operatorul: ')
    return op


def conversie(mesaj_input: str):
    nr = input(f'{mesaj_input}')
    while nr.isdigit() is False:
        nr = input(f'{mesaj_input}')
    return int(nr)


def calculator():
    nr_1 = conversie("Primul numar: ")
    nr_2 = conversie("Al doilea numar: ")
    op = operator()
    if op == '+':
        rezultat = add(nr_1, nr_2)
    elif op == '-':
        rezultat = subtract(nr_1, nr_2)
    elif op == '*':
        rezultat = multiply(nr_1, nr_2)
    elif op == '/':
        rezultat = divide(nr_1, nr_2)
    return rezultat
    # return f'{nr_1} {op} {nr_2} = , eval(f'{nr1} {op} {nr2})'


print(calculator())