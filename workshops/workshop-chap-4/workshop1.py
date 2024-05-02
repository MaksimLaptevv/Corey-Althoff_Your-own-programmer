def func(x):          # takes x - integer
    return x**2       # returns its square
b=0
while b==0:           # loop to check an integer number
    try:
        a=int(input('enter num: '))
        b+=1
    except ValueError:
        print('error')
print(a,'^2 = ',func(a),sep='')