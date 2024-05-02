def func_one(x):  # entering an integer parameter x and dividing it by 2
    return x//2

def func_two(y):  # entering an integer parameter y and multiplying it by 4
    return y*4

b=0

while b==0:       # loop for correct number entry
    try:
        a=int(input('enter num: '))
        b+=1
    except ValueError:
        print('enter int num!!')

x=func_one(a)
print(a,'/',2,'=',x)

y=func_two(x)
print(x,'*',4,'=',y)