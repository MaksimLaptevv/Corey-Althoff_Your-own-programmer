class triangle:
    def __init__(self,a,h):
        self.a=a
        self.h=h
    def area(self):
        return (self.a*self.h)/2

triangle1=triangle(5,3)
print(triangle1.area())