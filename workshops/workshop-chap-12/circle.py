import math

class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r*math.pow(math.pi,2)

circle1=circle(1)
print('S(r=1) =',circle1.area())