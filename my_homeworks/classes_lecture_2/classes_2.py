# 1. Make the class with composition.
class Laptop:
    def __init__(self, name, charge):
        self.name = name
        self.battery = Battery(charge)


class Battery:
    def __init__(self, charge):
        self.charge = charge


laptop = Laptop('lenovo', 87)
print(f'Laptop {laptop.name} has {laptop.battery.charge}% charge')
# result --> Laptop lenovo has 87% charge


# 2. Make the class with aggregation
class Guitar:
    def __init__(self, brand, *count_string):
        self.brand = brand
        self.count_string = [x for x in count_string]


class GuitarString:
    def __init__(self, count, name):
        self.count = count
        self.name = name


string1 = GuitarString(1, 'Prima')
string2 = GuitarString(2, 'Alt')
balalaika = Guitar('VASCO', string1, string2)
print(f'Balalaika {balalaika.brand} have {len(balalaika.count_string)} strings')
# result --> Balalaika VASCO have 2 strings

del balalaika
print(f'We have 2 strings - {string1.name} and {string2.name}')
# result --> We have 2 strings - Prima and Alt

# 3. Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
# Note: this method should be static
class Calc:

    @staticmethod
    def add_nums(x, y, z):
        return x+y+z


print(f'Sum of given parameters = {Calc.add_nums(5, 10, 4)}')
# result --> Sum of given parameters = 19

# 4*. Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def ingredients(self):
        return self

    @staticmethod
    def carbonara():
        return ['forcemeat', 'tomatoes']

    @staticmethod
    def bolognaise():
        return ['bacon', 'parmesan', 'eggs']

pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingredients == ["tomato", "cucumber"])
# result --> True
pasta_2 = Pasta.carbonara()
print(f'Pasta_2 has the following ingredients -{pasta_2}')
# result --> Pasta_2 has the following ingredients -['forcemeat', 'tomatoes']
pasta_3 = Pasta.bolognaise()
print(f'Pasta_3 has the following ingredients -{pasta_3}')
# result --> Pasta_3 has the following ingredients -['bacon', 'parmesan', 'eggs']

# 5*. Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.

class Concert:
    def __init__(self):
        self.max_visitor_num = 0
        self.visitor_num = 0


    @property
    def visitors_count(self):
        return self.visitor_num


    @visitors_count.setter
    def visitors_count(self, value):
        self.visitor_num = value if value <= self.max_visitor_num else self.max_visitor_num


concert_Imaging_Dragons = Concert()
concert_Imaging_Dragons.max_visitor_num = 10000
concert_Imaging_Dragons.visitors_count = 20000
print(f'The Imaging Dragons concert was attended {concert_Imaging_Dragons.visitors_count}')
# result --> The Imaging Dragons concert was attended 10000

concert_Hardkiss = Concert()
concert_Hardkiss.max_visitor_num = 10000
concert_Hardkiss.visitors_count = 6000
print(f'The Hardkiss concert was attended {concert_Hardkiss.visitors_count}')
# result --> The Hardkiss concert was attended 6000

# 6. Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

grandfather_address_book = AddressBookDataClass(0, 'John', '+840201521418', 'California Street', 'Travolta@gmail.com', '18/02/1954', 68)
print(grandfather_address_book)
# result --> AddressBookDataClass(key=0, name='John', phone_number='+840201521418', address='California Street', email='Travolta@gmail.com', birthday='18/02/1954', age=68)

# # 7. Create the same class (6) but using NamedTuple
from collections import namedtuple

NewAddressBookDataClass = namedtuple('NewAddressBookDataClass', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

grandmother_address_book = NewAddressBookDataClass(0, 'Madonna', '+840202457912', 'California Street', 'Madonna@gmail.com', '16/08/1958', 63)
print(grandmother_address_book)
# result --> NewAddressBookDataClass(key=0, name='Madonna', phone_number='+840202457912', address='California Street', email='Madonna@gmail.com', birthday='16/08/1958', age=63)

# 8. Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#    Make its str() representation the same as for AddressBookDataClass defined above.
#    Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')

class AddressBook:
    def __init__(self, key='', name='', phone_number='', address='', email='', birthday='', age=''):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age


    def __str__(self):
        return f"AddressBook(key='{self.key}', name='{self.name}', phone_number='{self.phone_number}', address='{self.address}', email='{self.email}', birthday= '{self.birthday}', age='{self.age}')"

address_book = AddressBook('0', 'John', '+840201521418', 'California Street', 'Travolta@gmail.com', '18/02/1954', '68')
print(address_book)
# result --> AddressBook(key='0', name='John', phone_number='+840201521418', address='California Street', email='Travolta@gmail.com', birthday= '18/02/1954', age='68')


# 9. Change the value of the age property of the person object
class Person:
    name = "John"
    age = 36
    country = "USA"

Person.age = 45
print(Person.age)
# result --> 45


# 10. Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


setattr(Student, "email", "canada@gmail.com")
email = getattr(Student, "email")
print(email)
# result --> canada@gmail.com

# # 11*. By using @property convert the celsius to fahrenheit
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature


    @property
    def temperature(self):
        return self._temperature * 1.8 +32


ottava = Celsius(25)
print(ottava.temperature)
# result --> 77.0
