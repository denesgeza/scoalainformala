import pandas as pd

dict_date = {
    'masini': ['Dacia', 'Volvo', 'Renault'],
    'culoare': ['rosu', 'alb', 'verde']
}

variabila = pd.DataFrame(dict_date)
print(variabila)
print()
# serie
masini = ['Dacia', 'Volvo', 'Renault']
var_2 = pd.Series(masini)
print(var_2)

print(var_2[0])
print()
# alocare de index
var_3 = pd.Series(masini, index=['x', 'y', 'z'])
print(var_3)
print(var_3[2])
print(var_3['z'])

masini_2 = {
    'x': 'Dacia',
    'y': 'Renault',
    'z': 'Volvo'
}

var_4 = pd.Series(masini_2)
print(var_4)
print()
# restrangem afisarea
var_5 = pd.Series(masini_2, index=['x', 'z'])
print(var_5)

print()
var_6 = pd.DataFrame(dict_date)
print(var_6.loc[0])
print()
print(var_6.loc[[0, 1]])
print()

var_7 = pd.DataFrame(dict_date, index=['prod1', 'prod2', 'prod3'])
print(var_7.loc['prod1'])

data = {
    "prod_1": {
        "masini": "Dacia",
        "culoare": "rosu",
    },
    "prod_2": {
        "masini": "Renault",
        "culoare": "rosu",
    },
    "prod_3": {
        "masini": "Volvo",
        "culoare": "rosu"
    }
}

var_8 = pd.DataFrame(data)
print(var_8)

fisier = var_8.to_csv('data.csv')

print()

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://api.exchangerate-api.com/v4/latest/USD'
var_9 = pd.read_json(url)
print(var_9)