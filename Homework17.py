"""Задание 1
Реализуйте класс «Автомобиль». Необходимо хранить
в полях класса: название модели, год выпуска, произво-
дителя, объем двигателя, цвет машины, цену. Реализуйте
методы класса для ввода данных, вывода данных, реа-
лизуйте доступ к отдельным полям через методы класса."""


class Vehicle:
    model = ''
    year = ''
    manufacturer = ''
    volume = ''
    color = ''
    price = ''

    def input_model(self, model):
        self.model = model

    def input_year(self, year):
        self.year = year

    def input_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def input_volume(self, volume):
        self.volume = volume

    def input_color(self, color):
        self.color = color

    def input_price(self, price):
        self.price = price

    def __str__(self):
        return f'\nModel: {self.model} \nYear: {self.year}\nManufacturer: {self.manufacturer}\nVolume: {self.volume}' \
               f'\nColor: {self.color}\nPrice: {self.price} $\n'


Zaz = Vehicle()
Zaz.input_model('Tavria')
Zaz.input_year(1995)
Zaz.input_manufacturer('Zaz')
Zaz.input_volume(1.1)
Zaz.input_color('red')
Zaz.input_price(700)
print(Zaz)

AM = Vehicle()
AM.input_model('DB9')
AM.input_year(2010)
AM.input_manufacturer('Aston Martin')
AM.input_volume(5.0)
AM.input_color('silver')
AM.input_price(40000)
print(AM)

"""Задание 2
Реализуйте класс «Книга». Необходимо хранить в
полях класса: название книги, год выпуска, издателя,
жанр, автора, цену. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса."""

class Book:
    name = ''
    year = ''
    publisher = ''
    genre = ''
    author = ''
    price = ''

    def input_name(self, name):
        self.name = name

    def input_year(self, year):
        self.year = year

    def input_publisher(self, publisher):
        self.publisher = publisher

    def input_genre(self, genre):
        self.genre = genre

    def input_author(self, author):
        self.author = author

    def input_price(self, price):
        self.price = price

    def __str__(self):
        return f'\nThe book {self.name} in genre {self.genre} was written by {self.author}, printed in {self.year} by' \
               f' {self.publisher} and it\'s price is {self.price} $\n'


WAP = Book()
WAP.input_name('War And Peace')
WAP.input_year(1992)
WAP.input_publisher('noname')
WAP.input_genre('roman')
WAP.input_author('Lev Tolstoy')
WAP.input_price(50)
print(WAP)

"""Задание 3
Реализуйте класс «Стадион». Необходимо хранить в
полях класса: название стадиона, дату открытия, страну,
город, вместимость. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса."""


class Stadium:
    name = ''
    date = ''
    country = ''
    city = ''
    capacity = ''

    def input_name(self, name):
        self.name = name

    def input_date(self, date):
        self.date = date

    def input_country(self, country):
        self.country = country

    def input_city(self, city):
        self.city = city

    def input_capacity(self, capacity):
        self.capacity = capacity

    def __str__(self):
        return f'The stadium \"{self.name}\" was built in {self.date} in the {self.city} of {self.country}' \
               f' and can contain {self.capacity} peoples'

Arena = Stadium()
Arena.input_name('Lviv Arena')
Arena.input_date(2011)
Arena.input_country('Ukraine')
Arena.input_city('Lviv')
Arena.input_capacity(34_725)

print(Arena)