# num_calls = 0
#
#
# def exercitiu(x):
#     global num_calls
#     num_calls = 3
#     num_calls += 1
#     return x * x
#
#
# print('1.', exercitiu(4))

def f(a, list=[]):
    for i in range(a):
        list.append(i*i)
    print(list)

f(3)
f(2, [1, 2, 3])
f(2)