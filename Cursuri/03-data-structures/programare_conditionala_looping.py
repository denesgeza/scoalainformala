# daca conditie:
#   print('adevarat)
# daca alta_conditie:
# print('nici aceasta nu e adevarata')
# altfel:
#   print('afisez doar daca 'conditie' si 'alta_conditie' nu sunt adevarate

my_var = 5
if my_var < 6:
    print('Set instructiuni #1')

elif my_var < 10:
    print('Set instructini #2')
else:
    print('Set instructiuni #3')
print('a iesit')

var = 1
while var < 10:
    print('bloc de instructiuni', var)
    var += 1


string = 'Ana are mere'
for i, v in enumerate( string):
    print(i, '=>', v)