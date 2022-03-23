class Clasa1:

    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip

    def schimbare_culoare(self, color):
        self.color = color

    def __str__(self):
        return f'Marca: {self.marca}, Tip: {self.tip}'


class Clasa2(Clasa1):

    def __init__(self, marca, tip):
        super().__init__(marca, tip)

    def scaune(self, incalzite=True):
        self.heated = incalzite

    def __str__(self):
        return f'{40*"="}\nMarca: {self.marca}, Tip: {self.tip}\nScaune incalzite: {self.heated}\n' \
               f'Culoare: {self.color}\n{40*"="}'


class Clasa3(Clasa1):

    def __init__(self, marca, tip):
        super().__init__(marca, tip)

    def faruri_led(self, leduri=False):
        self.led = leduri

    def __str__(self):
        return f'Marca: {self.marca}, Tip: {self.tip}, Leduri: {self.led}\n{40*"="}'


car_1 = Clasa2('Aro', 'M461')
car_1.scaune(False)
car_1.schimbare_culoare('Rosu')

car_2 = Clasa3('Dacia', '1310')
car_2.faruri_led(True)

print(car_1)
print(car_2)




