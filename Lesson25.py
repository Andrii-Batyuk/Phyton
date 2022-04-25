a = int(5)
b = str('Hello')

class Box:
    v = 5
    def open(self):
        print("Open box")

lanch = Box()
print(lanch.v)
lanch.open()

class Borsch:
    volume = 3
    color = 'red'
    components = ['Beetroot', 'Tomato', 'Meat', 'Potato']
    temperature = 20.5
    vegeterian = False
    create_date = '22/02/2022'
    life_period = 480
    def heating(self):
        self.temperature = self.temperature + 5
    def show_heating(self):
        return self.temperature
    def more_borsch(self):
        self.volume = self.volume + 1
    def show_volume_borsch(self):
        return self.volume

andrii_borsch = Borsch()
print(andrii_borsch.show_heating())
andrii_borsch.heating()
andrii_borsch.heating()
print(andrii_borsch.show_heating())
andrii_borsch.more_borsch()
print(andrii_borsch.show_volume_borsch())



