class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.top=None
    def travesal(self):
        temp=self.top
        while temp is not None:
            print(temp.data)
            temp=temp.next
        print("end of Stack")
    def push(self,value):
        if self.size()>=self.maxsize:
            print("stack overflow") 
            return
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.top==None:
            return -1
        else:
            data=self.top.data
            self.top=self.top.next
            print("book removed is:",data)
    def size(self):
        temp=self.top
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        return count
    def reverse(self):
        if self.maxsize<0:
            return
        a=[]
        while self.size:
            a=a+self.pop()
        print(a)
name=Stack(6)
name.push("p")
name.push("a")
name.push("n")
name.push("k")
name.push("a")
name.push("j")
name.travesal()
name.reverse()
