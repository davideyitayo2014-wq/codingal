# Circle class

class Circle:
    # Constructor - takes radius
    def __init__(self, radius):
        self.radius = radius

    # Method 1 - to find area
    def area(self):
        # Area = pi * r * r
        return 3.14 * self.radius * self.radius

    # Method 2 - to find perimeter (circumference)
    def perimeter(self):
        # Perimeter = 2 * pi * r
        return 2 * 3.14 * self.radius

# Create a circle object
r = float(input("Enter radius: "))
c1 = Circle(r)

# Display results
print("Radius:", c1.radius)
print("Area:", c1.area())
print("Perimeter:", c1.perimeter())