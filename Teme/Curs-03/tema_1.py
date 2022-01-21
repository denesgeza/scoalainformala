# TEMA 1.
# Să se scrie o funcție care primește un număr nedeﬁnit de parametrii și să se
# calculeze suma parametrilor care reprezintă numere întregi sau reale.
# 1. your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
# 2. your_function() va returna 0.
# 3. your_function(2, 4, 'abc', param_1 =2) va returna 6.


def my_sum(*args, **kwargs):
    result = 0
    for arg in args:
        if isinstance(arg, int):
            result += arg
    return result


def my_sum_2(*args, **kwargs):
    result = 0
    for arg in args:
        try:
            value = int(arg)
        except ValueError as e:
            pass
        except TypeError as e:
            pass
        else:
            result += value
    return result


# Checks
print(my_sum(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_sum_2(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_sum())
print(my_sum_2())
print(my_sum(2, 4, 'abc', param_1=2))
print(my_sum_2(2, 4, 'abc', param_1=2))
