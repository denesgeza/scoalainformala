def function(new_list):
    length = len(new_list)
    temp_list = new_list[-1]
    new_list[0] = new_list[length - 1]
    new_list[length - 1] = temp_list
    return new_list


param_list = [22, 11, 9, 44, 56]
print(function(param_list))


def functie_2(lista):
    item = 1
    for x, y in enumerate(lista):
        item *= x
        return lista[y + 1]


lista = [1, 2, 3]

print(functie_2(lista))

x = 1


def f():
    return x


print('1.', x)
print('2.', f())

x = [1, 2, 3, 4]
print('3.', x[-1:])

a = [1, 2, 3, 4]
b = [4, 5]
print('4.', a + b * 3)

def exercitiu(i):
    for i in range(i):
        return i

x = exercitiu(3)
print('5.', x)

def func(*args):
    return 3 + len(args)


print('6.', func(4, 4, 4))
