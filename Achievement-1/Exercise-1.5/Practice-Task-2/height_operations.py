class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f"{self.feet} feet, {self.inches} inches"

    def __add__(self, other):
        total_inches = (self.feet * 12 + self.inches) + (other.feet * 12 + other.inches)
        return Height(total_inches // 12, total_inches % 12)

    def __sub__(self, other):
        total_inches = (self.feet * 12 + self.inches) - (other.feet * 12 + other.inches)
        return Height(total_inches // 12, total_inches % 12)

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
height2 = Height(3, 8)
height3 = height1 - height2
print(f"Difference: {height3}")

