import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_point(self, point1, point2):
        dist = math.hypot(point1.getx(), point1.gety(), point2.getx(), point2.gety())
        return dist


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vert1 = vertice1
        self.__vert2 = vertice2
        self.__vert3 = vertice3

    def perimeter(self):
        d1 = Point.distance_from_point(self, self.__vert1, self.__vert2)
        d2 = Point.distance_from_point(self, self.__vert2, self.__vert3)
        d3 = Point.distance_from_point(self, self.__vert3, self.__vert1)
        sum = d1 + d2 + d3
        return sum


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
