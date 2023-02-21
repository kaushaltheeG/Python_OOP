#Abstract Base classses are used to enforce class constraints 

from abc import ABC, abstractclassmethod

#ABC is the abstract base class lib

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    #ensures every sub class will have an calcArea method or error will thrown 
    @abstractclassmethod
    def calcArea(self):
        pass 

class Circle(GraphicShape):
    def __init__(self,radius):
        self.radius = radius

    def calcArea(self):
        return (self.radius ** 2) * 3.14

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side 

    def calcArea(self):
        return self.side ** 2 


# g = GraphicShape()

c = Circle(10)
print(c.calcArea())

a = Square(13)
print(a.calcArea())