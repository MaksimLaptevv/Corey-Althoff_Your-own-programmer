list=[1,2,3,4,5,6,7,8,9,10]
c=0

while True:
    try:
        a=int(input('Enter number: '))
    except ValueError:
        print('Enter a NUMBER, not word')
        continue

    b=(c+1)%10

    if a!=b:
        print('No')
        c+=1
        continue

    else:
        print('Yes')
        print('YOU WIN!!!')
        break
