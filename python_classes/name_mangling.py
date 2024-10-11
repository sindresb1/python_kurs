# Another naming convention that you can see and use in Python classes is to add 
# two leading underscores to attribute and method names. This naming convention is
# triggers what's known as name mangling.

# Name mangling is an automatic name transformation that prepends the class's name to the
# member's name, like in _ClassName__atribute or _ClassName__method. This transformation
# reults in name hiding. In other words, mangled names aren't available for direct access
# and aren't part of a class's public API.

class SampleClass:
    def __init__(self, value):
        self.__value = value
    def __method(self):
        print(self.__value)

sample_instance = SampleClass("Hello")
print(vars(sample_instance))

print(vars(SampleClass))

sample_instance = SampleClass("Hello")
print(sample_instance.__value)

print(sample_instance.__method())

# In this class, .__value and .__method() have two leading underscores, so their names are namgled to 
# _SampleClass__value and _SampleClass__method. Because of this internal renaming, you can't access the
# attributes from outside the class using their original names.

# It is still possible to access name-mangled attributes or methods using their mangled names, although
# this is bad practice, and you should avoid it in your code.
print(sample_instance._SampleClass__value)
print(sample_instance._SampleClass__method())