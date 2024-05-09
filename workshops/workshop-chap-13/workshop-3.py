class shape:
    def what_am_i(self):
        print('Я - фигура.')

class rectangle(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calculate_perimetr(self):
        return self.a*2+self.b*2

class square(shape):
    def __init__(self,a):
        self.a=a
    def calculate_perimetr(self):
        return self.a*4

rectangle=rectangle(2,5)
square=square(6)

square.what_am_i()
rectangle.what_am_i()