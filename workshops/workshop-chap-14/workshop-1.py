class square:
    list_square=[]
    def __init__(self,area):
        self.area=area
        self.list_square.append(area)

s1=square(6)
s2=square(7)
s3=square(8)
print(square.list_square)