str=input('Любишь программировать?\n')

with open('file.txt', 'w') as file:
    file.write(str) #yes