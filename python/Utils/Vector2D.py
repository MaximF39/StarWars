import math


class Vector2D:

    def __init__(self, x, y, speed=None):
        self.x = x
        self.y = y
        if speed:
            self.speed = speed

    def distance(self, vector2):
        return ((self.x - vector2.x) ** 2 + (self.y - vector2.y) ** 2) ** 0.5

    def move(self, vector2, time):  # time
        """ vector2 - куда. time - время[c] """
        if self.speed == 0 or time == 0:
            return self
        atan = math.atan2(self.y - vector2.y, self.x - vector2.x)
        x = math.cos(atan) * self.speed * time
        y = math.sin(atan) * self.speed * time
        if self.x > vector2.x:
            x = self.x - x if self.x - x > vector2.x else vector2.x
        elif self.x < vector2.x:
            x = self.x - x if self.x - x < vector2.x else vector2.x
        else:
            x = vector2.x

        if self.y > vector2.y:
            y = self.y - y if self.y - y > vector2.y else vector2.y
        elif self.y < vector2.y:
            y = self.y - y if self.y - y < vector2.y else vector2.y
        else:
            y = vector2.y

        return Vector2D(x, y, self.speed)

    def time_wait(self, vector2):
        """ return second """
        return self.distance(vector2) / self.speed

    def in_radius(self, vector2, radius):
        length = ((self.x - vector2.x) ** 2 + (self.y - vector2.y) ** 2) ** 0.5
        if length > radius:
            return False
        return True

# player_vector = Vector2D(48, -397, 2)
# target_vector = Vector2D(-15.625654425557464, 2669.0, 0)
