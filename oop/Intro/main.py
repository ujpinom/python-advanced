import math
from DB import Database
import typing
class Point():

     def __init__(self, x: float = 0, y: float = 0) -> None:
          """
          Initialize the position of a new point. The x and y
          coordinates can be specified. If they are not, the
          point defaults to the origin.
          :param x: float x-coordinate
          :param y: float x-coordinate
          """
          self.move(x, y)

     def move(self, x:float,y:float) -> None:

          self.x=x
          self.y=y

     def reset(self):

          self.move(0,0)

     def calcular_dist(self,point:"Point") -> float:

          return math.hypot(self.x-point.x,self.y-point.y)
          db:Optional[Point]= None



a = Point()
b = Point()

a.move(5,0)
b.reset()

print(a.calcular_dist(b))