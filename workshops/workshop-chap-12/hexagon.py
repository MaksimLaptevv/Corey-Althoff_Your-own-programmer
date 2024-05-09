class hexagon:
    def __init__(self,a1,a2,a3,a4,a5,a6):
        self.a1=a1
        self.a2=a2
        self.a3=a3
        self.a4=a4
        self.a5=a5
        self.a6=a6
    def calculate_perimetr(self):
        return self.a1+self.a2+self.a3+self.a4+self.a5+self.a6

hexagon1=hexagon(1,1,1,1,1,1)
print(hexagon1.calculate_perimetr())