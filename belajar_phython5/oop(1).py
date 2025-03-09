import math
class Circle:
    def __init__(self, radius, color):
        self.__radius = radius
        self.__color = color
        
    def getRadius(self):
        return self.__radius
    
    def setRadius(self,radius):
        self.__radius = radius
    
    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color = color
    
    def getArea(self):
        return math.pi * self.__radius ** 2
    

# radius = 2, color = blue
c1 = Circle(2,"blue")
# c1.setRadius(2)
# c1.setColor("blue")
print(c1.getArea())

# radius = 2, color = red
c2 = Circle(2,"red")
# c2.setRadius(2)
# c2.setColor("red")
print(c2.getArea())

# radius = 1, color = red
c3 = Circle(1,"red")
# c3.setRadius(1)
# c3.setColor("red")
print(c3.getArea())