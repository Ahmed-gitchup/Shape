import math


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class ShapeUtils:
    @staticmethod
    def print_area(shape):
        area = shape.calculate_area()
        print("Area:", area)

    @staticmethod
    def print_perimeter(shape):
        perimeter = shape.calculate_perimeter()
        print("Perimeter:", perimeter)


# Prompt the user to enter the values for each shape
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

side1 = float(input("Enter the length of the first side of the triangle: "))
side2 = float(input("Enter the length of the second side of the triangle: "))
side3 = float(input("Enter the length of the third side of the triangle: "))
triangle = Triangle(side1, side2, side3)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)

# Use the helper methods to print the area and perimeter

print("-"*50)
print("This is a circle info:")
ShapeUtils.print_area(circle)
ShapeUtils.print_perimeter(circle)
print("-"*50)
print("This is a triangle info:")
ShapeUtils.print_area(triangle)
ShapeUtils.print_perimeter(triangle)
print("-"*50)
print("This is a rectangle info:")
ShapeUtils.print_area(rectangle)
ShapeUtils.print_perimeter(rectangle)