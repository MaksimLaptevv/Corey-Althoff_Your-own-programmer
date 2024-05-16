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

stack=stack()
for i in 'Позавчера':
    stack.push(i)
reverse=''
for i in range(len(stack.items)):
    reverse+=stack.pop()
print(reverse)