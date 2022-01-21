# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă
# aceasta este un număr întreg, altfel returnează valoarea 0.
def my_input():
    prompt = input('Introdu un numar ')
    try:
        value = int(prompt)
    except ValueError as e:
        return print(0)
    return print(value)


my_input()
