# Understanding Callable Objects in Python

print(dir(abs))

print(dir(all))

def greet():
    print('Hello World')

print(dir(greet))

greet.__call__()

class SampleClass:
    def method(self):
        print("You called method()!")

print(type(SampleClass))

print(dir(type))

sample_instance = SampleClass()
print(dir(sample_instance.method))

# Checking Whether an Object is Callable

print(callable(abs))

print(callable(all))

print(callable(greet))

print(callable(SampleClass))

print(callable(sample_instance))

class NonCallable:
    def __init__(self):
        raise TypeError("not really callable")
    
instance = NonCallable()
print(callable(instance))

instance()

# Creating Callable Instances with .__call__() in Python

