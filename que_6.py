#Define a class Vector with attributes x and y. Overload the + operator to add
#two Vector objects. Implement the __add__() method and test it by adding
#two Vector instances.

class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,t):

        return(vector(self.x+t.x,self.y+t.y))
    def __str__(self):
        return f"{self.x}, {self.y}"
    

v_1=vector(2,4)
v_2=vector(4,5)
print(v_1+v_2)
print(v_2)
print(v_1)