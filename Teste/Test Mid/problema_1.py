# 1. Scrie un program care sa calculeze suma dintre trei numere. Daca valorile sunt egale, returnati de trei ori suma acestora.(1 punct)

def adunare(a, b, c):
    if a == b == c:
        return 3 * (a + b + c)
    return a + b + c


print(adunare(2, 4, 5))
print(adunare(2, 2, 2))
print(adunare(2.2, 2.2, 2.2))

