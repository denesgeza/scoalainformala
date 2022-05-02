# 1. Să se scrie un program care gestionează o listă de mașini.
# O mașină este reprezentată ca dicționar și conține următoarele chei:
# -  id (identificator unic) - se va genera de către program (îl generați programatic)
#
# -  brand
#
# -  model hp (horse power)
#
# -  price
#
#
#
# Mașinile sunt catalogate în funcție de numărul de cai putere astfel: ○ slow_cars - mașinile cu numărul de cai putere < 120. ○ fast_cars - mașinile cu numărul de cai putere ≥ 120, dar < 180 ○ sport_cars - mașinile cu numărul de cai putere ≥ 180. ● Mașinile sunt catalogate în funcție de preț astfel: ○ cheap - mașinile cu prețul < 1000 ○ medium - mașinile cu prețul ≥ 1000, dar < 5000 ○ expensive - mașinile cu prețul ≥ 5000.
#
# Să se scrie un program care conține următoarele funcționalități: ○ citește datele de intrare dintr-un fișier aflat în fișierul input .csv
#
# ○ generează un folder output_data care va conține următoarele fișiere .json: ➠ slow_cars.json - conține datele despre toate mașinile care se încadrează în categoria slow_cars. ➠ fast_cars.json - conține datele despre toate mașinile care se încadrează în categoria fast_cars. ➠ sport_cars.json - conține datele despre toate mașinile care se încadrează în categoria sport_cars. ➠ cheap_cars.json - conține datele despre toate mașinile care se încadrează în categoria cheap. ➠ medium_cars.json - conține datele despre toate mașinile care se încadrează în categoria medium. ➠ expensive_cars.json - conține datele despre toate mașinile care se încadrează în categoria expensive. ➠ câte un fișier care conține toate datele despre un anumit brand de mașină. Ex: opel.json va conține toate datele despre mașinile al căror proprietate brand are valoarea Opel. ● La o rulare a programului, output-ul va fi valabil DOAR pentru datele curente. Fișierele vechi nu vor trebui să existe.

import json

stock = {}
with open('input.csv') as f:
    f.readline()
    id = 0
    for row in f:
        car = row.strip().split(',')
        id += 1
        car_details = {str(car[0] + ' ' + car[1]): {'id': id, 'brand': car[0], 'model': car[1], 'hp': car[2], 'price': car[3]}}
        stock.update(car_details)

brands = []
slow_cars = {}
fast_cars = {}
sport_cars = {}
cheap_cars = {}
medium_cars = {}
expensive_cars = {}
for car, car_details in stock.items():
    if stock[car]['brand'] not in brands:
        brands.append(car_details['brand'])
    # sort by hp
    if int(stock[car]['hp']) < 120:
        slow_cars.update({car: car_details})
    elif int(stock[car]['hp']) >= 120 and int(stock[car]['hp']) < 180:
        fast_cars.update({car: car_details})
    else:
        sport_cars.update({car: car_details})
    # sort by price
    if int(stock[car]['price']) < 1000:
        cheap_cars.update({car: car_details})
    elif int(stock[car]['price']) >= 1000 and int(stock[car]['price']) < 5000:
        medium_cars.update({car: car_details})
    elif int(stock[car]['price']) >= 5000:
        expensive_cars.update({car: car_details})

for car in brands:

    for k, v in stock.items():
        if v['brand'] == car:
            try:
                with open(car + '.json',) as f:
                    cars = json.load(f)
                    cars[k] = v
                    with open(car + '.json', 'w') as f:
                        json.dump(cars, f)
            except FileNotFoundError:
                with open(car + '.json', 'w') as f:
                    cars = {k: v}
                    json.dump(cars, f)


with open('slow_cars.json', 'w') as f:
    json.dump(stock, f)
with open('fast_cars.json', 'w') as f:
    json.dump(fast_cars, f)
with open('sport_cars.json', 'w') as f:
    json.dump(sport_cars, f)
with open('cheap_cars.json', 'w') as f:
    json.dump(cheap_cars, f)
with open('medium_cars.json', 'w') as f:
    json.dump(medium_cars, f)
with open('expensive_cars.json', 'w') as f:
    json.dump(expensive_cars, f)



