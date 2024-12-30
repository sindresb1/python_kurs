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