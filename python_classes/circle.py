import math

class Circle:
    """The .__init__() method has a special meaning in Python classes.
     This method is known as the object initializer because it defines and 
     sets the initial values for the object's attributes."""
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
    

# Note: In Python , the first argument of most methods is self. 
# This argument holds a reference to the current object so that you can use it inside the class.