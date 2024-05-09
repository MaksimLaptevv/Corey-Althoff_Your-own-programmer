class rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calculate_perimetr(self):
        return self.a*2+self.b*2

class square:
    def __init__(self,a):
        self.a=a
    def calculate_perimetr(self):
        return self.a*4

rectangle=rectangle(2,5) # p =14
square=square(5) # p = 20
list=[rectangle,square]

for f in list:
    print('P =',f.calculate_perimetr())
