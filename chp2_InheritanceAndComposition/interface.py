from abc import ABC, abstractclassmethod
#ABC is the abstract base class lib

#new base class that helps ensure that all the inherted class will have some implementation of toJSON() to prevent 
class JSONify(ABC):
    @abstractclassmethod
    #defines a 
    def toJSON(self):
        pass 

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    #ensures every sub class will have an calcArea method or error will thrown 
    @abstractclassmethod
    def calcArea(self):
        pass 

#takes in the the second base class; JSONify helps becuase we dont have to add toJSON() to GrpahicShape force me to add a toJSON() override even those those classes wont need it 
#power of multiple inheritance 
class Circle(GraphicShape, JSONify):
    def __init__(self,radius):
        self.radius = radius

    def calcArea(self):
        return (self.radius ** 2) * 3.14

    def toJSON(self):
        return f"{{\"circle\" : {str(self.calcArea())} }}"


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side 

    def calcArea(self):
        return self.side ** 2 


# g = GraphicShape()

c = Circle(10)
print(c.calcArea())
print(c.toJSON())

a = Square(13)
print(a.calcArea())