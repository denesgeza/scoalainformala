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
y = [x*x for x in a if x%2 == 0]
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
    # print('Hello Geek')


def ex(var):
    for letter in 'geeksforgeeks':
        if letter == 'e' or letter == 's':
            continue
        print('Current letter :', letter)
        var = 10
        return var


print('18.', ex(20))