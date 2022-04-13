import pandas as pd

print(pd.__version__)

a = {'x': 1, 'y': 7, 'z': 2}

variabila = pd.Series(a, index=['x', 'y'])
# variabila = pd.Series(a, index=a.keys())
print(variabila)

data = {
    'key1': [0, 1, 2],
    'key2': [4, 5, 6]
}

variabila_2 = pd.DataFrame(data, index=['linie1', 'linie2', 'linie3'])
print(variabila_2['key2'])  # print all values from key2

print(variabila_2.loc['linie2'])
