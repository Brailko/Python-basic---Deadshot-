
"""
Створіть клас робота пилососа
Робот пилосос має класові атрибути - обєм баку для сміття, обєм баку води
self атрибути - заповненість баку для сміття, заповненість баку для води, заряд батареї, серія/номер (ідентифікатор)
Заряд батареї у відсотках
заповнення баків для води і сміття - число
наприклад
Обєм баку для сміття - 1500
заповнений обєм - 340
1. ----
Реалізувати проперті - info, яке повертає інформацію про поточний стан робота

Приклад
"VR-1234183; power - 95%; water tank - 35%; trash tank - 76%
де VR-1234183 - серія/номер
-----
2. -----
реалізувати класи ексепшинів LowBattery, FullTrashTank, EmptyWatterTank
-----

3. -----
Реалізуйте функцію start_cleaning, функція може приймати параметр wet_cleaning: bool і time: int

функція запускає прибирання
прибирання це по суті цикл на time ітерацій
на кожній ітерації циклу - може викликатись 2 чи 3 функції

функція_1 - зменшення заряду батареї
робить перевірку який відсоток батареї на даний момент
якщо 5% і менше - кидає ексепшн LowBattery
якщо більше 5% - зменшує відсоток батареї на 2%

функція_2 - заповнення сміттєбака
завдяки модулю рандом, отримуємо число від 0 до 20 - це значення додаткового обєму сміття

робить перевірку заповненості баку сміття,
якщо поточна заповненість баку == обєму баку - кидає ексепшн FullTrashTank
якщо поточна заповненість баку != обєму баку
але при цьому поточна заповненість баку + додатковий обєм сміття >= обєму баку - то виставити значення поточної заповненості баку
як максимальне (обєм баку)
у всіх інших випадках - збільшити заповненість баку на число яке рандомили (додатковий обєм сміття)

функція_3 - вологе прибирання
запускається тільки якщо wet_cleaning is True
робить перевірку заповненості баку для води,
якщо бак для води пустий - кинути ексепшин EmptyWatterTank
якщо бак для води не пустий - зменшити значення поточної заповнненості баку води на 20
якщо після зменшення у вас стало відємне число - то перезаписати на 0 і кинути ексепшн EmptyWatterTank

в циклі в якому викликаються дані 3 функції повинна бути конструкція try except для опрацювання ексепшинів
ексепшини LowBattery, FullTrashTank - зупиняють прибирання
ексепшин EmptyWatterTank - зупиняє тільки вологе прибирання
якщо прибирання закінчилось достроково функція start_cleaning - повертає False
якщо прибирання достроково не закінчувалось функуція start_cleaning - повертає True
-----

4. -----
добавте логи в start_cleaning
лог - "VR-1234183; power - 95%; water tank - 60%; trash tank - 2% STARTED CLEANING"
лог - згенеровано певний ексепшн
лог - "VR-1234183; power - 0%; water tank - 2%; trash tank - 76% FINISHED CLEANING"

-----

ТЕСТИ!
використовуючи бібліотеки unittest або pytest напишіть тести для робота

тест-кейси які потрібно перевірити
1. повне прибирання на яке вистачає ресурсів
2. прибирання без вологого прибирання на яке вистачає ресурсів
3. прибирання під час якого не вистачило заряду батареї (перевірити що start_cleaning повернула False і що заряд батареї 0%)
4. прибирання під час якого заповнився сміттє бак (перевірити що start_cleaning повернула False і що сміттєбак повний)
5. прибирання під час якого не вистачило води (перевірити що start_cleaning повернула False і що бак з водою пустий)
6. проперті info повертає правильне значення

бонус завдання і тест кейси які можна перевірити (не обовязкові)
1. при створенні обєкта робота, заряд батареї не може бути меншим ніж 0 і більшим ніж 100
якщо в конструктор передали значення яке не не входить в діапазон 0-100 - кинути ексепшн ValueError
написати тести які перевірить що при правильно переданих значеннях обєкт створюється, при не правильних - кидається ексепшин

те ж саме можна опрацювати і перевірити для значення баків для сміття і води - (заповненість баку не повинна бути більша ніж обєм і менша ніж 0)

2. створіть обєкт робота, але при тестуванні викликайте на пряму функція_1, функція_2, функція_3
створіть тести які перевірять що при певних значеннях буде кидатись ексепшн

"""


class VacuumCleaner:
    pass

