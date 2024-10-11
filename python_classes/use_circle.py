from circle import Circle

# To create an object of a Python class like Circle, you must call the Circle()
# class constructor with a pair of parentheses and a set of appropriate arguments.
# What arguments? In Python, the class constructor accepts the same arguments as the __init__() method.
# In this example, the Circle class expects the radius argument.

# circle_1 and circle_" are separate instances of Circle.
circle_1 = Circle(42)
circle_2 = Circle(7)

print(circle_1)
print(circle_2)

# You access the object's attributes using the dot notation.
print(circle_1.radius)
print(circle_2.radius)

# You can also call the object's methods using the dot operator.
print(circle_1.calculate_area())
print(circle_2.calculate_area())

# You can also use dot notation and the assignment operator to change the current value of an attribute:
circle_1.radius = 100
print(circle_1.radius)
print(circle_1.calculate_area())

# Now the radius of circle_1 is entirely different. When you call -calculate_area(), the result immediately reflects this change.
# You've changed the object's internal state or date, which typically impacts its behaviors or methods.