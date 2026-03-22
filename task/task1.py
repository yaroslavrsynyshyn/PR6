class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print("Прямокутник 1:")
print("Площа:", rect1.area())
print("Периметр:", rect1.perimeter())

print("\nПрямокутник 2:")
print("Площа:", rect2.area())
print("Периметр:", rect2.perimeter())