import os
# Exceptions
# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# # Can put multiple exceptions on same line
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown")


# Cleaning up
# try:
#     file = open("app_build.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
    
# Can put multiple exceptions on same line
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown")
# # Note: finally clause always execute, used to release external resources (close files, database connections, network connections...etc.)
# finally:
#     file.close()

# try:
#     with open("dataStructures.py") as file:
#         print("File opened.")
#         age = int(input("Age: "))
#         xfactor = 10 / age
# except (ValueError, ZeroDivisionError, FileNotFoundError):
#     print("You didn't enter a valid age.")
#     print("File not found")
# else:
#     print("No exceptions were thrown")

# Raising Exceptions
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less.")
#     return 10 / age

# try:
#     calculate_xfactor(2)
# except ValueError as error:
#     print(error)

from timeit import timeit

code1 = """
# Cost of Raising Exceptions
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(2)
except ValueError as error:
    pass
"""

code2 = """
# Cost of Raising Exceptions
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))


