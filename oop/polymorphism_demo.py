import math

# Base class Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        # Rectangle area = length * width
        return self.length * self.width

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        # Circle area = π * radius^2
        return math.pi * (self.radius ** 2)
