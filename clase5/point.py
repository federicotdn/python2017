import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return '[x = ' + str(self.x) + ', y = ' + str(self.y) + ']'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Point(-self.x, -self.y)


print(Point())

print(Point(1, 1) == Point(1, 1))

print(Point(1, 2) + Point(3, 3))

print(-Point(1, 2))