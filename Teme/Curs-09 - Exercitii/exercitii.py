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

# print('12.', 'foo' + 2) # cannot concatenate str and int

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
# loop infinit cu Hello Greek


def ex(var):
    for letter in 'geeksforgeeks':
        if letter == 'e' or letter == 's':
            continue
        print('Current letter :', letter)
        var = 10
        return var


print('18.', ex(20))
# Current letter : g
# 10


def f(a, list=[]):
    for i in range(a):
        list.append(i*i)
    print(list)
print('20.')
f(3)
f(2, [1, 2, 3])
f(2)

#### 21.
list = ['1', '2', '3', '4', '5']
print('21.', list[12:])
# empty list


#### 22.
class ClasaMea:

    def Met1(self, a):
        global var1
        var1 = a


obj = ClasaMea()
obj.Met1('Salut Lume')

# Nu returneaza nimic, stocheaza var1='Salut Lume' in var1


#### 23.
class Test123():
    def __str__(self) -> str:
        self.x = 77777
        return str(self.x)

obj_test123 = Test123()
print('23.', obj_test123)
# 77777

#### 24.
class X(object):
    def Ad(self, a, b, c):
        return self.a + self.b + self.c

obiect1 = X()
# print('24.', obiect1.Ad(1, 2, 3))
# self.a, self.b, self.c NU sunt atributele clasei X ==> error

print('25.', 15*'-')
class test123():
    def rezultat(self):
        self.y = 77777

# obj_test124 = test123()
# print('25.', obj_test124.rezultat())
test123 = test123()
test123.y = 77777
print('25.', test123.y) #--> nu exista atributul y in clasa test123
print('25', type(test123))

#### 26.
print('26.', 15*'-')
class X(object):
    def Ad():
        print('Imi place Python')

obiect111 = X()
print(obiect111)

#### 27.
# print('27.')
# class Tsdf1234():
#     def __init__(self, x):
#         self.x = x
#
# asdf = Tsdf1234()

# --> missing 1 required positional argument: 'x'

#### 28.
print('28.')

#### 29.
print('29.', 15*'-')
class Test1():
    def Met1(self):
        self.unu = 'unu'
        return self.unu
class Test2(Test1):
    def Met2(self):
        self.unu = 'doi'
        return self.unu
class Test3(Test2):
    def Met2(self):
        self.doi = 'doi'

obj = Test2()
print('29.', obj.Met1(), obj.Met2())

#### 30.
print('30.', 15*'-')


class Test1():
    dinamic = 'ceva'
    def Met1(self):
        return Test1.dinamic.upper()

obj = Test1()
print(obj.Met1())

print(2//3)

jjj= []
print(str(jjj))

__str__ = 3
print(__str__)