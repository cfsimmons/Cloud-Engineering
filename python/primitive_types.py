course = "Python for Beginners     "
print(len(course))
print(course[0])
print(course[-1])
print(course[0:6]) #Python
print(course[7:20])

#frBgnes [this is limit:this is step: this is the step]...20 is the end..
# If string ends before 20, it will stop at the last character
print(course[7:40:2]) 

# String Methods (Everything in python is an object...objects are instances of classes)
# methods are functions that belong to objects
print("\n\n" + course.upper())
print(course.lower())
print(course.title())

# strip white spaces
print(len(course))
print(len(course.strip()))
print(len(course.lstrip()))
print(len(course.rstrip()))
print(course.find("pro")) # -1 means string not found
print(course.replace("Python", "Java")) # replace all occurrences of "Python" with "Java"
print("swift" not in course)

#input and type conversion
x = int(input("Enter a number: "))
y = x + 1
print(y)

print(int(x))
print(float(x))
print(bool(x))
print(str(x))
# ord - returns the ASCII value of a character
ord("d")

age = 22
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

message = "You are an adult." if age >= 18 else "You are not an adult."
print(message)