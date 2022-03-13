# import math
#
# x1, y1 = 0, 0
# x2, y2 = 0, 90
#
# y2_y1 = y2 - y1
# x2_x1 = x2 - x1
#
#
# angel = math.atan2(y2_y1, x2_x1)
#
# radius = abs(x2_x1 * math.cos(angel)) + abs(y2_y1 * math.sin(angel))
#
# print(math.degrees(angel))
# print(math.radians(math.degrees(angel)))
# print(angel)
# print(radius)

# class Base2:
#     def __init__(self, prefix:str, max_=1000, repair_speed: float = 0.1):
#         str_max_val = f"max{prefix.title()}"
#         self.__val = prefix
#         self.__dict__.update({
#             str_max_val: max_,
#             self.__val : max_,
#             'repair_speed': repair_speed,
#             f"restore": lambda: setattr(self, self.__val , getattr(self, str_max_val)),
#             f"repair": lambda: setattr(self, self.__val , getattr(self, self.__val ) - 100),
#         })
#
#     def __repr__(self):
#         return getattr(self, self.__val).__str__()
#
# class Health(Base2):
#
#     def __init__(self):
#         super().__init__(self.__class__.__name__.lower())
#
# class Energy(Base2):
#
#     def __init__(self):
#         super().__init__(self.__class__.__name__.lower())
#
# class B_Player:
#
#     def __init__(self):
#         self.health = Health()
#         self.energy = Energy()
#
# p = B_Player()
# p.health.repair()
# print(p.health) # 900
# p.health.restore()
# print(p.health) # 100

# p.energy.energy_repair()
# print(p.energy.ene)


# print(b.health)

# class Test:
#     def __str__(self):
#         return "STR"
#
#     def __repr__(self):
#         return "REPR"
#
#
# test = Test()
# print(test) # STR
# print(repr(test)) # REPR
# print([test]) # [REPR]
# print(str([test])) # [REPR]

# import sys
# print("What is your name?")
# same = sys.stdin.readline()