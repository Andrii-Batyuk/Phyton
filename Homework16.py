"""Курс: «Введение в язык
программирования Python
Модуль 10. Объектно-ориентированное
программирование
Тема: Классы. Объекты
Задание 1
Реализуйте класс «Человек». Необходимо хранить в
полях класса: ФИО, дату рождения, контактный телефон,
город, страну, домашний адрес. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса."""


class Human:
    name = str()
    surname = str()
    birthdate = int()
    phone = int()
    city = str()
    country = str()
    address = str()

    def input_name(self):
        self.name = input("Input name: ")
        if not self.name:
            self.name = "Name not set"
        while self.name.isnumeric() or (len(self.name) < 3) or (len(self.name) > 75):
            self.name = input("You input wrong name, please try again: ")

    def input_surname(self):
        self.surname = input("Input surname: ")
        if not self.surname:
            self.surname = "Surname not set"
        while self.surname.isnumeric() or (len(self.surname) < 3) or (len(self.surname) > 75):
            self.surname = input("You input wrong surname, please try again: ")

    def input_birthdate(self):
        self.birthdate = input("Input birthdate, format [01.01.2000]: ")
        if not self.birthdate:
            self.birthdate = 'Birthday not set'

    def input_phone_number(self):
        self.phone = input("Input phone number, format +380xxxxxxxxx: ")
        if not self.phone:
            self.phone = 'Phone number not set'

    def input_city(self):
        self.city = input("Input city: ")
        if not self.city:
            self.city = 'City not set'


    def input_country(self):
        self.country = input("Input country: ")
        if not self.country:
            self.country = 'Country number not set'


    def input_address(self):
        self.address = input("Input address: ")
        if not self.address:
            self.address = 'Address not set'


    def input_info(self):
        self.input_name()
        self.input_surname()
        self.input_birthdate()
        self.input_phone_number()
        self.input_city()
        self.input_country()
        self.input_address()

    def print_info(self):
        print(f'Name: {self.name}')
        print(f'Surname: {self.surname}')
        print(f'Birthdate: {self.birthdate}')
        print(f'Phone: {self.phone}')
        print(f'City: {self.city}')
        print(f'Country: {self.country}')
        print(f'Address: {self.address}')


# man = Human()
# print('Input man\'s information')
# man.input_info()
# man.print_info()
# woman = Human()
# print('Input woman\'s information')
# woman.input_info()
# woman.print_info()


"""
Задание 2
Создайте класс «Город». Необходимо хранить в по-
лях класса: название города, название региона, название
страны, количество жителей в городе, почтовый индекс
города, телефонный код города. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса."""


class City:
    name = ''
    region = ''
    country = ''
    postalcode = ''
    phone_code = ''

    def input_name(self):
        self.name = input("Input city name: ")
        if not self.name:
            self.name = "Name not set"
        while self.name.isnumeric() or (len(self.name) < 3) or (len(self.name) > 75):
            self.name = input("You input wrong city name, please try again: ")

    def input_region(self):
        self.region = input("Input city region: ")
        if not self.region:
            self.region = "Region not set"
        while self.region.isnumeric() or (len(self.region) < 3) or (len(self.region) > 75):
            self.region = input("You input wrong city region, please try again: ")

    def input_country(self):
        self.country = input("Input country: ")
        if not self.country:
            self.country = "Country not set"


    def input_postalcode(self):
        self.postalcode = input("Input postalcode: ")
        if not self.postalcode:
            self.postalcode = "Postalcode not set"


    def input_phone_code(self):
        self.phone_code = input("Input phone code: ")
        if not self.phone_code:
            self.phone_code = "Phone code not set"

    def input_info(self):
        self.input_name()
        self.input_region()
        self.input_country()
        self.input_postalcode()
        self.input_phone_code()

    def print_info(self):
        print(f'Name: {self.name}')
        print(f'Region: {self.region}')
        print(f'Country: {self.country}')
        print(f'Postalcode: {self.postalcode}')
        print(f'Phone code: {self.phone_code}')



# Nikolaev = City()
# Nikolaev.input_info()
# Nikolaev.print_info()
# Odessa = City()
# Odessa.input_name()
# Nikolaev.print_info()


""" Задание 3
Создайте класс «Страна». Необходимо хранить в
полях класса: название страны, название континента,
количество жителей в стране, телефонный код страны,
название столицы, название городов страны. Реализуйте
методы класса для ввода данных, вывода данных, реа-
лизуйте доступ к отдельным полям через методы класса."""

continents = ['Asia', 'Europe', 'Australia', 'North America', 'South America']


class Country:
    name = ''
    continent = ''
    population = ''
    phone_code = ''
    capital = ''
    cities = ''

    def input_name(self):
        self.name = input("Input country name: ")
        if not self.name:
            self.name = "Name not set"
        while self.name.isnumeric() or (len(self.name) < 3) or (len(self.name) > 75):
            self.name = input("You input wrong country name, please try again: ")

    def input_continent(self):
        while self.continent not in continents:
            self.continent = input("Input continent: ")
        if not self.continent:
            self.continent = "Continent not set"

    def input_population(self):
        self.population = input("Input population: ")
        if not self.population:
            self.population = "Population not set"

    def input_capital(self):
        self.capital = input("Input capital of country: ")
        if not self.capital:
            self.capital = "Capital not set"
        while self.capital.isnumeric() or (len(self.capital) < 3) or (len(self.capital) > 75):
            self.capital = input("You input wrong capital, please try again: ")

    def input_cities(self):
        self.cities = input("Input cities name: ")
        if not self.cities:
            self.cities = "Cities not set"
        while self.cities.isnumeric() or (len(self.cities) < 3) or (len(self.cities) > 75):
            self.cities = input("You input wrong cities name, please try again: ")

    def input_info(self):
        self.input_name()
        self.input_continent()
        self.input_population()
        self.input_capital()
        self.input_cities()

    def print_info(self):
        print(f'Name: {self.name}')
        print(f'Continent: {self.continent}')
        print(f'Population: {self.population}')
        print(f'Capital: {self.capital}')
        print(f'Cities: {self.cities}')


# Ukraine = Country()
# Ukraine.input_info()
# Ukraine.print_info()


""" Задание 4
Создайте класс «Дробь». Необходимо хранить в полях
класса: числитель и знаменатель. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса. Также создайте
методы класса для выполнения арифметических опера-
ций (сложение, вычитание, умножение, деление, и т.д.)"""

class Fraction:
    numerator = int()
    denominator = int()
    def __init__(self, number):
        self.numerator = int(number[:number.find('/')])
        self.denominator = int(number[number.find('/')+1:])

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        n1 = self.numerator * other.denominator
        n2 = self.denominator * other.denominator
        n3 = other.numerator * self.denominator
        n4 = other.denominator * self.denominator
        denominator = n2
        numerator = n1 + n3
        return f'{numerator}/{denominator}'

    def decimation(self):
        return self.numerator/self.denominator

    def __mul__(self, other):

        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.numerator
        return f'{numerator}/{denominator}'

    def __sub__(self, other):
        a1 = self.numerator * other.denominator
        a2 = self.denominator * other.denominator
        a3 = other.numerator * self.denominator
        numerator = a1 - a3
        denominator = a2
        return f'{numerator}/{denominator}'

    def __truediv__(self, other):
        b1 = self.numerator * other.denominator
        b2 = self.denominator * other.numerator
        numerator = b1
        denominator = b2
        return f'{numerator}/{denominator}'




d = Fraction('11/24')
e = Fraction('5/11')
print(d)
print(e)
print(d,'+',e,'=', d+e)

h = Fraction(d+e)
print(h)
print(h.decimation())
a = Fraction('34/23')
b = Fraction('25/17')
print(a)
print(b)
print(a, '*', b, '=', a*b)
h = Fraction(a*b)
print(h.decimation())

c = Fraction('46/63')
d = Fraction('36/74')
print(c)
print(d)
print(c, '-', d, '=', c-d)
h = Fraction(a-b)
print(h.decimation())

e = Fraction('8/15')
f = Fraction('3/13')
print(e)
print(f)
print(e, '/', f, '=', e/f)
h = Fraction(e/f)
print(h.decimation())