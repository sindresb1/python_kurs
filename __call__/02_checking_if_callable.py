def greet():
    print('Hello World')

class SampleClass:
    def method(self):
        print("You called method()!")

sample_instance = SampleClass()

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