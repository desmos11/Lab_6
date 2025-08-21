#Create a base class Shape with a method area(). Derive two classes
#Rectangle and Circle from Shape. Implement the area() method in both
#derived classes. Instantiate Rectangle and Circle, and demonstrate
#polymorphism by calling their area() methods.

import math as m
class SHAPE:
    def __init__(self):
        pass

    def area(self):
        return(0)
    
class circle(SHAPE):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return(m.pi*self.radius**2)
    
class rectangle(SHAPE):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return(self.l*self.b)
    
c=circle(1)
print(c.area())
r=rectangle(2,3)
print(r.area())
    
