class stack:
    def __init__(self):
        self.items=[]
    '''def isEmpty(self):
        return self.items==[]'''
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    '''def peek(self):
        last=len(self.items)-1
        return last'''
    '''def size(self):
        return len(self.items)'''

list1=[1,2,3,4,5]

list2=[]

stack=stack()

for item in list1:
    stack.push(item)

for i in range(len(stack.items)):
    list2.append(stack.pop())
print(list2)