list1=[8,19,148,4]
list2=[9,1,33,83]

list_ans=[]
for i in list1:
    for j in list2:
        res=i*j
        list_ans.append(res)

print(list_ans)