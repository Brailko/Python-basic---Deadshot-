# TASK 1
# Створити логер який дозволяє працювати з файлами як звичайний open,
# але разом з тим в файл logs.txt записує:
# коли був відкритий файл, назва файла, коли закритий файл
# для інформації про час можемо використати datetime.now()
# приклад відпрацювання
# with my_custom_manager('file.txt', 'r') as f:
#     f.read()
# В файл буде записано
# 2022-07-11 22:17:59.782551 file.txt OPEN
# 2022-07-11 22:18:00.782551 file.txt CLOSE
import csv
from datetime import datetime
import csv


class My_Manager():
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.file = open(self.filename, mode)
        with open('logs.txt', 'a') as f:
            f.write(f'{datetime.now()} {filename} OPEN\n')

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        with open('logs.txt', 'a') as f:
            f.write(f'{datetime.now()} {self.filename} CLOSE\n')

with My_Manager('Hello.txt', 'w') as manager:
    manager.write('Hello people\n')
    manager.write('How are you?\n')

with My_Manager('Capital.txt', 'w') as manager:
    manager.write('Kyiv is the capital of Ukraine\n')

with My_Manager('Python.txt', 'w') as manager:
    manager.write('Programming in Python is fun\n')

# TASK 2
# Написати ф-цію яка переводить файл logs.txt в logs.csv
# Приклад такого файлу
# 2022-07-11 22:17:59.782551, file.txt, OPEN
# 2022-07-11 22:18:00.782551, file.txt, CLOSE

def translate_txt_in_csv():
    with open('logs.txt', 'r') as f_txt:
        with open('logs.csv', 'w') as f_csv:
            writer = csv.writer(f_csv, delimiter=' ')
            for str_txt in f_txt:
                writer.writerow(str_txt.split())

translate_txt_in_csv()

# TASK 3 (з зірочкою)
# Написати ф-цію, яка обраховує з файла logs.csv скільки раз був відкритий файл і його остання дата відкриття.
# Цю інформацію записати в logs.json. Приклад:
# {
#     "file.txt": {
#         "count": 2,
#         "last_time_opened": "2022-07-11 22:17:59.782551"
#     }
# }


# P.S. Якщо щось не зрозуміло по умові задачі, то робіть як вважаєте за доцільно,
# користуючись здоровим глуздом звичайно ж)