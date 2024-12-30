# If you want the instances of a given class to be callable, then you need to implement the
# .__call__() special method in the underlying class. This method enables you to call the
# instances of your class as you'd call regular functions.

# Unlike other special methods, .__call__() doesn’t have special requirements for what arguments 
# it must accept. It works like any other instance method in the sense that it takes self as its 
# first argument and can take as many extra arguments as you need.

# counter.py
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def __call__(self):
        self.increment()

counter = Counter()
counter.increment()
print(counter.count)
counter()
print(counter.count)
counter()
print(counter.count)

# power.py
class PowerFactory:
    def __init__(self, exponent=2):
        self.exponent = exponent

    def __call__(self, base):
        return base**self.exponent

square_of = PowerFactory(2)
print(square_of(3))
print(square_of(6))

cube_of = PowerFactory(3)
print(cube_of(3))
print(cube_of(6))