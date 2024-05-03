def func_one(x):  # entering an integer parameter x and dividing it by 2
    return x//2

def func_two(y):  # entering an integer parameter y and multiplying it by 4
    return y*4

a = int(input())

y = func_one(a)
x = func_two(y)
print(x)
