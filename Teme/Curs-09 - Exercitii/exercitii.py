num_calls = 0


def exercitiu(x):
    global num_calls
    num_calls = 3
    num_calls += 1
    return x * x


print('1.', exercitiu(4))


x = 1
def f():
    return x

print('2.', x, f())

x = [1, 3, 'hello', 'world', ['another', 'list']]
print('3.', len(x[3]))

x = (1, 2, 3)
# x[1] = 4  # tuple doesnt support item assignment

# print('4.', print(x))

a = [1, 2, 3]
b = [4, 5]

print('5.', a + b * 3)

x = [1, 2, 3, 4]

print('6.', x[-1:])

x = [0, 1, [2]]
x[2][0] = 3
x[2].append(4)
x[2] = 2


print('7.', x)
# 8
def exercitiu8(i):
    for i in range(i):
        return i

x = exercitiu8(3)
print('8.', x)

a = range(10)
y = [x * x for x in a if x % 2 == 0]
print('9.', y)


def make_account():
    return {'balance': 0}


def deposit(account, amount):
    account['balance'] += amount
    return account['balance']


a = make_account()
print('10.', deposit(a, 10))


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

a = BankAccount()
print('11.', a.deposit(100))

# print('12.', 'foo' + 2) # canot concatenate str and int

try:
    print('a')
except:
    print('b')
else:
    print('c')
finally:
    print('d')


for k in {'x': 1, 'y': 2}:
    print('14.', k)

print('15.', list('python'))


def func(*args):
    return 3 + len(args)


print('16.', func(4, 4, 4))

# count = (3, 2, 5, 4)
# while len(count) < 5:
#     count0 = count[0] + 1
#     print('Hello Geek')


def ex(var):
    for letter in 'geeksforgeeks':
        if letter == 'e' or letter == 's':
            continue
        print('Current letter :', letter)
        var = 10
        return var


print('18.', ex(20))


def f(a, list=[]):
    for i in range(a):
        list.append(i*i)
    print(list)

f(3)
f(2, [1, 2, 3])
f(2)


class ClasaMea:

    def Met1(self, a):
        global var1
        var1 = a


obj = ClasaMea()
obj.Met1('Salut Lume')

class Test123():
    def __str__(self) -> str:
        self.x = 77777
        return str(self.x)

obj_test123 = Test123()
print('23.', obj_test123)

class X(object):
    def Ad(self, a, b, c):
        self.a = a
        self.b = b
        return self.a + self. b

obiect1 = X()
print('24.', obiect1.Ad(1, 2, 3))


class test123():
    def rezultat(self):
        self.x = 77777


# # ???
# obj_test124 = test123()
# a = obj_test124.rezultat()
#
# test123.y = 77777
# print('25.', test123.y)
# # print('25.', abc)
#
#
# class Y(object):
#     def Ad(self):
#         print('Imi place Python')
#
# obiect111 = X()
# print(obiect111)

# class Tsdf1234():
#     def __init__(self, x):
#         self.x = x
#
# asdf = Tsdf1234()

class Test1():
    dinamic = 'ceva'
    def Met1(self):
        return Test1.dinamic.upper()

obj = Test1()
obj.Met1()

