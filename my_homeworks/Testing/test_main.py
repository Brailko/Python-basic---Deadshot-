import pytest

from my_homeworks.Testing.exceptions import LowBattery, FullTrashTank, EmptyWatterTank
from my_homeworks.Testing.main import VacuumCleaner


# 1. повне прибирання на яке вистачає ресурсів
def test_full_wet_cleaning():
	test_cleaner = VacuumCleaner(0, 340, 100, "VR-1234183")
	assert test_cleaner.start_cleaning(True, 17) == True
	assert test_cleaner.start_cleaning(True, 18) == False


# 2. прибирання без вологого прибирання на яке вистачає ресурсів
def test_full_dry_cleaning():
	test_cleaner = VacuumCleaner(0, 340, 100, "VR-1234183")
	assert test_cleaner.start_cleaning(False, 48) == True
	assert test_cleaner.start_cleaning(False, 49) == False


# 3. прибирання під час якого не вистачило заряду батареї (перевірити що start_cleaning повернула False і що заряд батареї 0%)
def test_discharge():
	test_cleaner = VacuumCleaner(0, 340, 100, "VR-1234183")
	assert test_cleaner.start_cleaning(False, 49) == False
	assert test_cleaner.battery_charge <= 5


# 4. прибирання під час якого заповнився сміттє бак (перевірити що start_cleaning повернула False і що сміттєбак повний)
def test_full_garbage_tank():
	test_cleaner = VacuumCleaner(1485, 340, 100, "VR-1234183")
	assert test_cleaner.start_cleaning(False, 4) == False
	assert test_cleaner.full_garbage_tank == test_cleaner.volume_garbage_tank


# 5. прибирання під час якого не вистачило води (перевірити що start_cleaning повернула False і що бак з водою пустий)
def test_empty_water_tank():
	test_cleaner = VacuumCleaner(1400, 59, 100, "VR-1234183")
	assert test_cleaner.start_cleaning(True, 3) == False
	assert test_cleaner.full_water_tank == 0


# 6. проперті info повертає правильне значення
def test_info():
	test_cleaner = VacuumCleaner(1400, 61, 100, "VR-1234183")
	info = 'Identifier - VR-1234183; power - 100%; water tank - 18%; trash tank - 93%'
	assert test_cleaner.info == info


# 1. при створенні обєкта робота, заряд батареї не може бути меншим ніж 0 і більшим ніж 100
# якщо в конструктор передали значення яке не не входить в діапазон 0-100 - кинути ексепшн ValueError
# написати тести які перевірить що при правильно переданих значеннях обєкт створюється, при не правильних - кидається ексепшин
# те ж саме можна опрацювати і перевірити для значення баків для сміття і води - (заповненість баку не повинна бути більша ніж обєм і менша ніж 0)
def test_garbage_water_charge_norm():
	test_cleaner = VacuumCleaner(1400, 61, 100, "VR-1234183")
	assert test_cleaner.full_garbage_tank == 1400

def test_garbage_error():
	with pytest.raises(ValueError):
		VacuumCleaner(1600, 61, 100, "VR-1234183")

def test_water_error():
	with pytest.raises(ValueError):
		VacuumCleaner(1400, -2, 100, "VR-1234183")

def test_charge_error():
	with pytest.raises(ValueError):
		VacuumCleaner(1400, 61, 120, "VR-1234183")

# 2. створіть обєкт робота, але при тестуванні викликайте на пряму функція_1, функція_2, функція_3
# створіть тести які перевірять що при певних значеннях буде кидатись ексепшн

def test_discharge_battery():
	test_cleaner = VacuumCleaner(1500, 0, 0, "VR-1234183")
	with pytest.raises(LowBattery):
		test_cleaner.discharge_battery()

def test_filling_garbadge_tank():
	test_cleaner = VacuumCleaner(1500, 0, 0, "VR-1234183")
	with pytest.raises(FullTrashTank):
		test_cleaner.filling_garbadge_tank()


def test_empty_water_tank():
	test_cleaner = VacuumCleaner(1500, 0, 0, "VR-1234183")
	with pytest.raises(EmptyWatterTank):
		test_cleaner.empty_water_tank()


if __name__ == '__main__':
	pytest.main()
