# 1. Create a class Vehicle with Attributes: name, max_speed, and total_capacity.
class Vehicle:
    def __init__(self, name, brand, max_speed, total_capacity):
        self.name = name
        self.brand = brand
        self.max_speed = max_speed
        self.total_capacity = total_capacity


# 1. Method: fare. It should calculate the price of the trip.
    def fare(self):
        return self.total_capacity * 100


# 2. Create classes Bus that inherit Vehicle.
class Bus(Vehicle):
# 7. Write a magic method to Bus that would be triggered when len() function is called. Play around with other dunder methods
    def __str__(self):
        return f'{self.brand} {self.name} has maximum speed {self.max_speed} and can accommodate {self.total_capacity} passengers'


    def __len__(self):
        return self.total_capacity//3


# 6. Add used_capacity attribute for Bus.
    def count_of_passengers(self, used_capacity):
        if used_capacity > self.total_capacity:
            return f'Error: number of passengers {used_capacity}, and seats in {self.brand} {self.name} only {self.total_capacity}. You need to order another vehicle'
        else:
            return f'Go to trip!!!'


# 5. Override fare method for Bus class. Here we need to add an extra 10% to the fare.
    def fare(self):
        return self.total_capacity * 110


# 2. Create classes Car that inherit Vehicle.
class Car(Vehicle):
    pass


# 8. Create class Engine with attribute volume and method get_volume() that will return volume.
# 9. Inherit Engine by Car class.
class Engine(Car):
    volume = 1.6

    def get_volume(self):
        return self.volume


# 3. Create 3 car objects
car_1 = Car('Coupe', 'Smart', 135, 1)
car_2 = Car('Passat', 'Volkswagen', 232, 4)
car_3 = Car('Grand Scenic', 'Renault', 190, 6)

# 3. Create 2 bus objects
bus_1 = Bus('Sprinter', 'Mercedes', 170, 16)
bus_2 = Bus('Mago', 'Iveco', 130, 31)

# 4. Check: if car_1 is instance of Car.
print(isinstance(car_1, Car))
# result --> True

# 4. Check: if car_2 is instance of Vehicle.
print(isinstance(car_2, Vehicle))
# result --> True

# 4. Check: if bus_1 is instance of Car. if bus_1 is instance of Vehicle
print(isinstance(bus_1, Car))
# result --> False

# 4. Check: if bus_1 is instance of Vehicle
print(isinstance(bus_1, Vehicle))
# result --> True

# 5. Fare on vehicles
print(f'The cost of a trip by {car_1.brand} {car_1.name} is {car_1.fare()}$')
# result --> The cost of a trip by Smart Coupe is 100$

print(f'The cost of a trip by {car_2.brand} {car_2.name} is {car_2.fare()}$')
# result --> The cost of a trip by Volkswagen Passat is 400$

print(f'The cost of a trip by {car_3.brand} {car_3.name} is {car_3.fare()}$')
# result --> The cost of a trip by Renault Grand Scenic is 600$

print(f'The cost of a trip by {bus_1.brand} {bus_1.name} is {bus_1.fare()}$')
# result --> The cost of a trip by Mercedes Sprinter is 1760$

print(f'The cost of a trip by {bus_2.brand} {bus_2.name} is {bus_2.fare()}$')
# result --> The cost of a trip by Iveco Mago is 3410$

# 6. Add used_capacity attribute for Bus
print(bus_1.count_of_passengers(18))
# result --> Error: number of passengers 18, and seats in Mercedes Sprinter only 16. You need to order another vehicle
print(bus_2.count_of_passengers(26))
# result --> Go to trip!!!

# 7. Write a magic method to Bus that would be triggered when len() function is called. Play around with other dunder methods
print(bus_1)
# result --> Mercedes Sprinter has maximum speed 170 and can accommodate 16 passengers
print(bus_2)
# result --> Iveco Mago has maximum speed 130 and can accommodate 31 passengers
print(f'The length of the {bus_1.name} is {len(bus_1)} metrs')
# result --> The length of the Sprinter is 5 metrs
print(f'The length of the {bus_2.name} is {len(bus_2)} metrs')
# result --> The length of the Mago is 10 metrs


# 10. Check what is inheritance order of the Car class
print(f"Engine is inherit of Car - {issubclass(Engine, Car)}")
# result --> Engine is inherit of Car - True