#Define a class Time with attributes hours, minutes, and seconds. Overload
#the == operator to compare two Time objects for equality. Implement the
#__eq__() method and test it by comparing two Time instances.


class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __eq__(self, other):
        if (self.h == other.h) and (self.m == other.m) and (self.s == other.s):
            return True
        else:
            return False



t1 = Time(10, 30, 45)
t2 = Time(10, 30, 45)
t3 = Time(9, 15, 20)

print(t1 == t2)  
print(t1 == t3) 

