
class VacuumCleaner():
    volume_garbage_tank = 1500
    volume_water_tank = 340

    def __init__(self, full_garbage_tank, full_water_tank, battery_charge, id):
        self.full_garbage_tank = full_garbage_tank
        self.full_water_tank = full_water_tank
        self.battery_charge = battery_charge
        self.id = id

    def info(self):
        return (f"Identifier - {self.id}; power - {self.battery_charge}%; "  
               f"water tank - {round(self.full_water_tank * 100 / self.volume_water_tank)}%; "
               f"trash tank - {round(self.full_garbage_tank * 100 / self.volume_garbage_tank)}%")


thomas = VacuumCleaner(1140, 119, 95, 'VR-1234183')

print(thomas.info())