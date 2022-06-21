#1. Define the id of next variables:
int_a = 55
print(id(int_a)) # 140729069739376
str_b = 'cursor'
print(id(str_b)) # 2033900733296
set_c = {1, 2, 3}
print(id(set_c)) # 2033900938624
lst_d = [1, 2, 3]
print(id(lst_d)) # 2033902815040
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e)) # 2033895699200

#2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d = [1, 2, 3]
lst_d.append(4)
lst_d.append(5)
print(lst_d) # [1, 2, 3, 4, 5]
print(id(lst_d)) # 2033902814080

# 3. Define the type of each object from step 1.
print(type(int_a)) # <class 'int'>
print(type(str_b)) # <class 'str'>
print(type(set_c)) # <class 'set'>
print(type(lst_d)) # <class 'list'>
print(type(dict_e)) # <class 'dict'>

# 4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int)) #True
print(isinstance(str_b, str)) #True
print(isinstance(set_c, set)) #True
print(isinstance(lst_d, list)) #True
print(isinstance(dict_e, dict)) #True

# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(3, 4))
# Anna has 3 apples and 4 peaches.

# 6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(3, 4))
# Anna has 4 apples and 3 peaches.

# 7. By using keyword arguments into the curly braces.
print("Anna has {apple_count} apples and {peache_count} peaches.".format(apple_count=2, peache_count=6))
# Anna has 2 apples and 6 peaches.

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format(3, 4))
# Anna has     3 apples and   4 peaches.

# 9. With f-strings and variables
apple = 6
peache =10
print(f"Anna has {apple} apples and {peache} peaches.")
# Anna has 6 apples and 10 peaches.

# 10. With % operator
apple = 2
peache =9
print("Anna has %s apples and %s peaches." % (apple, peache))
# Anna has 2 apples and 9 peaches.

# 11*. With variable substitutions by name (hint: by using dict)
print("Anna has %(apple_count)d apples and %(peache_count)d peaches." % {'apple_count': 1, 'peache_count': 6})
# Anna has 1 apples and 6 peaches.

# 12. Convert (1) to list comprehension
lst = [num**2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13. Convert (2) to regular for with if-else
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension)
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

# 14. Convert (3) to dict comprehension.
d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d)
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15*. Convert (4) to dict comprehension.
d1 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d1)
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

# 16. Convert (5) to regular for with if.
dict_comprehension = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension[x] = x ** 3
print(dict_comprehension)
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# 17*. Convert (6) to regular for with if-else.
dict_comprehension_1 = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension_1[x] = x**3
    else:
        dict_comprehension_1[x] = x
print(dict_comprehension_1)
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
print(foo(2, 4))
# 2

# 19*. Convert (8) to regular function
def foo_1(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo_1(2, 4, 5))
# 4

# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
print(lst_to_sort)
# [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort(reverse=True)
print(lst_to_sort)
# [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(list(map(lambda x: x*2, lst_to_sort)))
# [10, 36, 2, 48, 66, 30, 26, 110]

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print(list(map(lambda x, y: x+y, list_A, list_B)))
# [7, 9, 11]

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(list(filter(lambda x: x % 2 == 1, lst_to_sort)))
# [5, 1, 33, 15, 13, 55]

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
print(list(filter(lambda x: x < 0, b)))
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
print(list(filter(lambda x: x in list_2, list_1)))
# [2, 3, 5, 7]


