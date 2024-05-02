def func(x,y,z,f=8,g=7):   # takes three mandatory (x,y,z) and two optional parameters (f,g), all parameters are integer
    return x+y+z+f+g
b=0
list_int_nums=[]
while b==0:                # a cycle to check the correctness of the three required parameters entered by the user
    try:
        str=input('enter 3 nums, separated by commas: ')
        nums_str=str.split(',')
        if nums_str.__len__()>3 or nums_str.__len__()<3:
            print('enter 3 nums!!!!')
            continue
        for i in range(3):
            list_int_nums.append(int(nums_str[i]))
        b+=1
    except ValueError:
        print('error')
print(list_int_nums[0],'+',list_int_nums[1],'+',list_int_nums[2],'+',8,'+',7,'=',func(list_int_nums[0],list_int_nums[1],list_int_nums[2]))