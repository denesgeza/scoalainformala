# Option 1
with open('fisier.txt', 'w') as file:
    file.write('Buna seara')

#  OPTION 2
file = open('fisier.txt', 'w')
file.write('Buna')
file.close()

# Option 3
file = open('fisier.txt', 'w')
try:
    file.write('Buna ziua')
# except Exception:
#     pass
finally:
    file.close()

# Option 4

with open('fisier1.txt', 'a') as file:
    file.write('Noapte buna')


with open('fisier1.txt', 'r') as file:
    for line in file.readlines():
        print('line', line)

with open('fisier1.txt', 'r') as file:
    for line in list(file):
        print('line', line)

