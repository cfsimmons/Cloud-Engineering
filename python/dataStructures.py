from array import array

items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 30),
]

prices = []
for item in items:
    prices.append(item[1])

lambda_prices = lambda items: [item[1] for item in items]

# map: do something to element 
map_prices = map(lambda item: item[1]*2, items)

print(lambda_prices(items))  

for item in map_prices:
    print(item)

print()

# lambda example
def square(x):
    return x * x

# lambda parameter: expression
lambda_square = lambda x: x * x

print(lambda_square(5))

# filter: remove items you dont want 
x = list(filter(lambda item: item[1] >= 10, items))

# expression for item in items - item itself
x = [item for item in items if item[1] >= 10]
print(dict(x))

list1 = [1,2,3]
list2 = [10,20,30]

# Zip Function
[(1,10), (2,20), (3,30)]
print(list(zip("xyz", list1, list2)))
"""Output:
    [('x', 1, 10), ('y', 2, 20), ('z', 3, 30)]
"""

# Stack
# LIFO (Last In First Out)
print("Stack Example")
browsing_session = []

browsing_session.append(1)
browsing_session.append(2)
print(browsing_session)

# Tuples (immutable)
point = (1, 2) + (3, 4)
print(type(point))

point = tuple([1,2])
print(point)

# Variable Swap
x = 10
y = 11
z = x
print(x)
print(y)

x = y
y = z
print(x)
print(y)

# Arrays (only for LARGE list of numbers)
# numbers = array("i", [1, 2, 3])
# numbers[0] = 1.0

# Sets - unordered set of unique items
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second) # {1, 2, 3, 4, 5}
print(first & second) # {1} items in first and second set
print(first - second) # {2, 3, 4} diff between 2 sets
print(first ^ second) # {2, 3, 4, 5}

# Dictionaries

point = {"x": 1, "y": 2}
point = dict(x=1,y=2)
print(point["x"])

point["x"] = 10
point["y"] = 20

if "a" in point:
    print(point["a"])
print(point.get("a", 0))

# del point["x"]
# print(point)

for key, value in point.items():
    print(key, value)
    
# Dictionary Comprehensions
values = []
for x in range(5):
    values.append(x * 2)
    
    
values = {x: x * 2 for x in range(5)}
print(values)

# Generator Object
values = (x * 2 for x in range(5))
print(values)

from sys import getsizeof

values = [x * 2 for x in range(1000)]
print(f"{getsizeof(values)}")

# Unpacking operator
first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(f"values: {values}")

numbers = [1, 2, 3]
print(*numbers)
print(1, 2, 3)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)


sentence = "This is a common interview question"

char_frequency = {}

for char in sentence:
    print(f"char: {char}")
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(f"value counts: {char_frequency}")