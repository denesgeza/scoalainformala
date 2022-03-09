# TEMA 1.
# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se
# calculeze suma parametrilor care reprezintă numere întregi sau reale.
# 1. your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
# 2. your_function() va returna 0.
# 3. your_function(2, 4, 'abc', param_1 =2) va returna 6.


def my_sum(*args):
    result = 0
    for arg in args:
        try:
            if isinstance(arg, int):
                result += arg
        except TypeError:
            continue
        except ValueError:
            continue
       
    return result


def my_sum_2(*args):
    result = 0
    for arg in args:
        try:
            value = int(arg)
        except ValueError:
            pass
        except TypeError:
            continue
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
