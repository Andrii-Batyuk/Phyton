

class Vehicle:
    model = ''
    year = ''
    manufacturer = ''
    volume = ''
    color = ''
    price = ''

    def __init__(self, model, year, manufacturer, volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.volume = volume
        self.color = color
        self.price = price

    def __str__(self):
        return f'Model: {self.model} \nYear: {self.year}\nManufacturer: {self.manufacturer}\nVolume: {self.volume}' \
               f'\nColor: {self.color}\nPrice: {self.price} $\n'


Audi = Vehicle('A6', 2005, 'Audi', 2.0, 'Gray', 4500)
print(Audi)
Lada = Vehicle('Niva', 2000, 'Lada', 1.7, 'White', 2500)
print(Lada)

