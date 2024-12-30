# The .__init__() method is the instance initializer. Python calls this method 
# automatically whenever you create an instance of a class by calling the class
#  constructor. The arguments to .__init__() will be the same as the arguments to
#  the class constructor, and they’ll typically provide initial values for instance 
# attributes.

# Meanwhile, the .__call__() method turns instances into callable objects. As you
#  already learned, Python automatically calls this method whenever you call a 
# concrete instance of a given class.


class Demo:
    def __init__(self, attr):
        print(f"Initialize an instance of {self.__class__.__name__}")
        self.attr = attr
        print(f"{self.attr = }")

    def __call__(self, arg):
        print(f"Call an instance of {self.__class__.__name__} with {arg}")

demo = Demo("Some initial value")

demo("Hello")