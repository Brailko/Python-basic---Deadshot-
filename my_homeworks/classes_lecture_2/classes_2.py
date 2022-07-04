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

# # 3.
# class Calc:
#     """
#     Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should be static
#     """
#
# # 4*.
# class Pasta:
#     """
#     Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """
#
# # 5*.
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """
#
# # 6.
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
#     """
#
# # 7. Create the same class (6) but using NamedTuple
#
#
# # 8.
# class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
#     """
# # 9.
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"
#
# # 10.
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
# # 11*.
# class Celsius:
#     """
#     By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)
#     """
#     def __init__(self, temperature=0):
#         self._temperature = temperature
#
#
# # create an object
# {obj} = ...
#
# print({obj}.temperature)
