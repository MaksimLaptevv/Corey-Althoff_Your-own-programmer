class square:
    def __init__(self,a):
        self.a=a

    def change_size(self,size):
        self.a=self.a+size
        return self.a

square=square(5)

print(square.change_size(0))
print(square.change_size(-3))
print(square.change_size(+10))