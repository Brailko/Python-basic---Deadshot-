# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers

class FibonacciNumbers:
    def __init__(self, count_numbers):
        self.count_numbers = count_numbers
        self.number_fibonachi = 0
        self.number_fibonachi_1 = 0
        self.number_fibonachi_2 = 1
        self.counter = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.counter > self.count_numbers:
            raise StopIteration
        if self.counter == 0:
            self.counter += 1
            return 0
        elif self.counter == 1:
            self.counter += 1
            return 1
        else:
            self.number_fibonachi = self.number_fibonachi_2 + self.number_fibonachi_1
            self.number_fibonachi_2, self.number_fibonachi_1 = self.number_fibonachi, self.number_fibonachi_2
            self.counter += 1
            return self.number_fibonachi


for i in FibonacciNumbers(10):
    print(i, end=' ')
# result --> 0 1 1 2 3 5 8 13 21 34 55
print()

# 2. Implement generator for Fibonacci numbers

def gener_fibonacci(count):
    yield 0
    yield 1
    number_fibonachi_1, number_fibonachi_2 = 0, 1
    while count - 1 > 0:
        number_fibonachi = number_fibonachi_2 + number_fibonachi_1
        number_fibonachi_1, number_fibonachi_2 = number_fibonachi_2, number_fibonachi
        count -= 1
        yield number_fibonachi


for i in gener_fibonacci(10):
    print(i, end=' ')
# result --> 0 1 1 2 3 5 8 13 21 34 55
print()

# 3. Write generator expression that returns square numbers of integers from 0 to 10
# Напишіть вираз-генератор, який повертає квадрати цілих чисел від 0 до 10

def square_gen(counter):
    for i in range(0, counter):
        yield i**2


for i in square_gen(11):
    print(i, end=' ')
# result --> 0 1 4 9 16 25 36 49 64 81 100
print()

# 4.Implement coroutine for accumulation arithmetic mean
# Реалізувати співпрограму для накопичення середнього арифметичного


def accumulation_mean():
    number = yield
    count = 1
    while True:
        mean = number / count
        number += yield mean
        count += 1


acc_mean = accumulation_mean()
next(acc_mean)
print(acc_mean.send(2))
# result --> 2
print(acc_mean.send(8))
# result --> 5
print(acc_mean.send(2))
# result --> 4
print(acc_mean.send(4))
# result --> 4