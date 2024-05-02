def func(str):   # a function with a string parameter and converting it to a floating point number if the string is incorrect, tells the user to enter the number correctly
    try:
        a=float(str)
    except ValueError:
        print('enter FLOAT OR INT, not str and etc.')
    return a
str=input('enter float or int: ')
print(func(str))