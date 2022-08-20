import pytest
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


if __name__ == '__main__':
	pytest.main()
