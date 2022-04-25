class WashingMachine:
    weight = 10
    count_of_water = 10
    color = 'white'
    electric_count = 100
    id = 1
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def __add__(self, other):#+
        self.weight = self.weight + other.weight

    def __int__(self):
        print("NOT INT")

    def __str__(self):
        return f'Weight : {self.weight}\nColor : {self.color}'
    def washing(self):
        print('Start wash')

    def drying(self):
        print('Start dry')

    def spining(self):
        print('Start wash')


bosch = WashingMachine(20, 'red')
noname = WashingMachine(70, 'red')
print(bosch.weight)
print(noname.weight)
bosch + noname
print(bosch.weight)
bosch + noname
print(bosch.weight)
a = 5
# int(bosch)
# bosch + a #not work
# bosch.count_of_water = 20
# print(bosch.count_of_water)
# print(bosch.color)
print(bosch)
s = str(bosch)
print(s)