# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
# #
# # point1 = Point()
# # point1.x = 10
# # point1.y = 20
# #
# # print(point1.x)
# # point1.draw()
# #
# # point2 = Point()
# # point2.x = 1
# # print(point2.x)
#
# point = Point(10,20)
# point.x = 14
# print(point.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self, message):
        print(f"{message}, i am {self.name}")

person = Person("huy")
person.talk("Hello")

person2 = Person("Thuc")
person2.talk("Hi ba con ")
