import math


class Vector2D:
    DEGREE_TO_RADIAN: float = 57.2957795130823
    x: float
    y: float
    length: float
    length2: float

    # def __init__(self, x=0, y=0):
    #     self.length = self.calculate_length(x, y)
    #     self.length2 = self.calculate_length2(x, y)

    def set_vector2D(self, x: float, y: float) -> None:
        """ save x and y"""
        self.x = x
        self.y = y

    @staticmethod
    def calculate_length2(x: float, y: float) -> float:
        """ i want the function to be name sum_pow """
        return x * x + y * y

    def calculate_length(self, p1: float, p2: float) -> float:
        """ length for between 2 points """
        return self.calculate_length2(p1, p2) ** 0.5

    @staticmethod
    def validate_angle(p1: float) -> float:
        """ does this so that p1 is between -pi and pi """
        while p1 < -math.pi:
            p1 += math.pi * 2
        while p1 > math.pi:
            p1 -= math.pi * 2
        return p1

    @staticmethod
    def validate_angle_in_degrees(p1: float) -> float:
        """ does this so that p1 is between -180 and 180 """
        while p1 < -180:
            p1 += 180 * 2
        while p1 > 180:
            p1 -= 180 * 2
        return p1

    @staticmethod
    def get_sector_angle(p1: float, p2: float) -> float:
        return p2 / p1

    def radian_to_degree(self, p1: float) -> float:
        return p1 * self.DEGREE_TO_RADIAN

    def degree_to_radian(self, p1: float) -> float:
        return p1 / self.DEGREE_TO_RADIAN

    @staticmethod
    def distance(sum_x: float, sum_y: float) -> float:
        """ return absolute length """
        return (abs(sum_x) ** 2 + abs(sum_y) ** 2) ** 0.5

    def set_members_by_vector(self, p1) -> None:
        """ set x and y x via 2d vector """
        self.x = p1.x
        self.y = p1.y

    def clone(self):
        """ clone vector2D """
        class_ = Vector2D()
        class_.set_vector2D(self.x, self.y)
        return class_

    def set_members(self, x: float, y: float) -> None:
        """ set x and y? why are there identical, repetitive """
        self.x = x
        self.y = y

    def add_vector(self, p1) -> None:
        """ add x and y via vector2D"""
        self.x += p1.x
        self.y += p1.y

    def add(self, p1: float, p2: float) -> None:
        """ just add x and y p1 and p2"""
        self.x += p1
        self.y += p2

    def subtract_vector(self, p1) -> None:
        self.x -= p1.x
        self.y -= p1.y

    def subtract(self, p1, p2):
        self.x -= p1
        self.y -= p2

    def multiply_vector(self, p1):
        self.x *= p1.x
        self.y *= p1.y

    def multiply(self, p1: float, p2: float):
        self.x *= p1
        self.y *= p2

    def add_vector_c(self, p1):
        class_ = Vector2D()
        class_.set_vector2D(self.x + p1.x, self.y + p1.y)
        return class_

    def subtract_vector_c(self, p1):
        class_ = Vector2D()
        class_.set_vector2D(self.x - p1.x, self.y - p1.y)
        return class_

    def multiply_c(self, p1):
        class_ = Vector2D()
        class_.set_vector2D(self.x * p1.x, self.y * p1.y)
        return class_

    def vector_projection_onto(self, p1):
        _loc2_ = Vector2D()
        _loc2_.get_unit_vector()
        _loc2_.multiply_c(self.scalar_projection_onto(p1))
        return _loc2_

    def get_unit_vector(self):
        # _loc1_ = self.length
        # # if _loc1_:
        # #     class_ = Vector2D()
        # #     class_.set_vector2D(self.x / _loc1_, self.y / _loc1_)
        #     return class_
        class_ = Vector2D()
        class_.set_vector2D(self.x, self.y)
        return class_

    def scalar_projection_onto(self, p1):
        return (self.x * p1.x + self.y * p1.y) / len(p1)

    def get_normal(self):
        """ return vector2D (-1 * y, x)"""
        class_ = Vector2D()
        class_.set_vector2D(-1 * self.y, self.x)
        return class_

    def get_opposite_to_normal(self):
        """ return vector2D (-y, -1 * x)"""
        class_ = Vector2D()
        class_.set_vector2D(-self.y, -1 * self.x)
        return class_

    def get_angle(self) -> float:
        """ gets the angle between two vectors between the vector and the... x axis, it seems.. """
        _loc1_ = math.atan2(self.y, self.x) + math.pi / 2
        return self.validate_angle(_loc1_)

    def get_angle_between(self, p1) -> float:
        """ i don''t know how it works
        well, they clearly packages_entrance the angle between a vector and some axis, and between two vectors. The only confusing
         part is what the angle of get_angle is counted from - that is, for which vectors the angle is zero.
         I think the answer is "for (-1,0) vectors", making it count the angle from the negative-y axis - which is
         pretty unconventional, normally in math you count from the positive x axis.
        """
        _loc2_ = p1.get_angle() - self.get_angle()
        return self.validate_angle(_loc2_)

    def get_angle_in_degrees(self) -> float:
        return self.radian_to_degree(self.get_angle())

    def set_members_by_ra(self, p1: float, p2: float) -> None:
        self.set_members_by_rac(p1, p2, 0, 0)

    def rotate_to(self, p1: float) -> None:
        self.set_members_by_rac(self.length, self.get_angle() + p1, 0, 0)

    def rotate_to_degrees(self, p1: float) -> None:
        self.set_members_by_rac(self.length, self.get_angle() + self.degree_to_radian(p1), 0, 0)

    def set_members_by_rac(self, p1: float, p2: float, p3: float, p4: float) -> None:
        p2 -= math.pi / 2
        self.x = p1 * math.cos(p2) + p3
        self.y = p1 * math.sin(p2) + p4
