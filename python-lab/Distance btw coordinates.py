#Program to return distance between 2 points on a cartesian plane.
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        """print(self.getx())
        print(self.gety())
        print(x)
        print(y)"""
        dist = math.hypot(self.__x, self.__y, x, y)
        return dist

    def distance_from_point(self, point):
        """print(self.getx())
        print(self.gety())
        print(point.getx())
        print(point.gety())"""
        dist = math.hypot(self.__x, self.__y, point.getx(), point.gety())
        return dist

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
