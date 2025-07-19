class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f"{self.feet} feet, {self.inches} inches"

    def __lt__(self, other):
        return (self.feet * 12 + self.inches) < (other.feet * 12 + other.inches)

    def __le__(self, other):
        return (self.feet * 12 + self.inches) <= (other.feet * 12 + other.inches)

    def __eq__(self, other):
        return (self.feet * 12 + self.inches) == (other.feet * 12 + other.inches)

    def __gt__(self, other):
        return (self.feet * 12 + self.inches) > (other.feet * 12 + other.inches)

    def __ge__(self, other):
        return (self.feet * 12 + self.inches) >= (other.feet * 12 + other.inches)

    def __ne__(self, other):
        return (self.feet * 12 + self.inches) != (other.feet * 12 + other.inches)

height1 = Height(5, 10)
height2 = Height(5, 9)
height3 = Height(6, 1)

print(height1 > height2)  # True
print(height1 >= height2)  # True
print(height1 == height2)  # False
print(height1 != height2)  # True
print(height1 < height3)  # True
print(height1 <= height3)  # True

