class square:
    def __init__(self,a):
        self.a=a
    def __repr__(self):
        return '{} на {} на {} на {}'.format(self.a,self.a,self.a,self.a)

s1=square(5)
s2=square(10)
s3=square(50)
print(s1,s2,s3,sep='\n')