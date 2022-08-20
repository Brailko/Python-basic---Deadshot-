from random import randint
import logging
from my_homeworks.Testing import exceptions

logging.basicConfig(level=logging.INFO, filename='test.log')

class VacuumCleaner():
    volume_garbage_tank = 1500
    volume_water_tank = 340

    def __init__(self, full_garbage_tank, full_water_tank, battery_charge, id):
        if 0 <= full_garbage_tank <= self.volume_garbage_tank:
            self.full_garbage_tank = full_garbage_tank
        else:
            raise ValueError
        if 0 <= full_water_tank <= self.volume_water_tank:
            self.full_water_tank = full_water_tank
        else:
            raise ValueError
        if 0 <= battery_charge <= 100:
            self.battery_charge = battery_charge
        else:
            raise ValueError
        self.id = id


    @property
    def info(self):
        return f"Identifier - {self.id}; power - {self.battery_charge}%; " \
               f"water tank - {round(self.full_water_tank * 100 / self.volume_water_tank)}%; " \
               f"trash tank - {round(self.full_garbage_tank * 100 / self.volume_garbage_tank)}%"

    def start_cleaning(self, wet_cleaning: bool, time: int):
        logging.info(f"{self.info} STARTED CLEANING")
        for i in range(time):
            try:
                self.discharge_battery()
                self.filling_garbadge_tank()
            except exceptions.LowBattery as ex:
                logging.error(ex.message)
                logging.info(f"{self.info} FINISHED CLEANING")
                return False
            except exceptions.FullTrashTank as ex:
                logging.error(ex.message)
                logging.info(f"{self.info} FINISHED CLEANING")
                return False
            if wet_cleaning:
                try:
                    self.empty_water_tank()
                except exceptions.EmptyWatterTank as ex:
                    logging.error(ex.message)
                    logging.info(f"{self.info} FINISHED CLEANING")
                    return False
        logging.info(f"{self.info} FINISHED CLEANING")
        return True


    def discharge_battery(self):
        if self.battery_charge <= 5:
            raise exceptions.LowBattery("Low battery. It is necessary to charge the device")
        else:
            self.battery_charge -= 2

    def filling_garbadge_tank(self):
        i = randint(1, 20)
        if self.full_garbage_tank >= self.volume_garbage_tank:
            raise exceptions.FullTrashTank('The garbage tank is full. Empty the tank')
        elif self.full_garbage_tank + i >= self.volume_garbage_tank:
            self.full_garbage_tank = self.volume_garbage_tank
        else:
            self.full_garbage_tank += i

    def empty_water_tank(self):
        if self.full_water_tank == 0:
            raise exceptions.EmptyWatterTank('Empty water tank. Pour water into the tank')
        else:
            self.full_water_tank -= 20
            if self.full_water_tank < 0:
                self.full_water_tank = 0
                raise exceptions.EmptyWatterTank('Empty water tank. Pour water into the tank')


# thomas = VacuumCleaner(1450, 59, 10, "VR-1234183")
thomas = VacuumCleaner(0, 340, 100, "VR-1234183")

print(thomas.info)

print(thomas.start_cleaning(False, 48))

