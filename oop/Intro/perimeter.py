import math
from typing import *

class NonPerimetro(Exception):
    pass

class Point():

    def __init__(self,x:float,y:float):

        self.x=x
        self.y = y

    def dist(self,other:'Point'):

        return math.hypot(self.x-other.x,self.y-other.y)



Pair = Tuple[float,float]

point_tupla = Union[Pair,Point]

class polygono():

    def __init__(self,puntos:point_tupla):

        self.verticesx: list[Point]= []

        if len(puntos)<=1:
            raise NonPerimetro('Perimetro no es posible ser calculado para un punto o ninguno')

        if puntos:

            for punto in puntos:

               self.verticesx.append(self.make_point(punto))

    def make_point(self,punto):

        return punto if isinstance(punto, Point) else Point(*punto)


    def perimetro(self):

        pares = zip(self.verticesx, self.verticesx[1:]+self.verticesx[:1])
        perimetro=0

        for p1,p2 in pares:

            perimetro+= p1.dist(p2)

        return perimetro


square = [(1,1), (1,2)]
try:
    s= polygono(square)
    print(s.perimetro())
except Exception as ex:

    print(*ex.args)





