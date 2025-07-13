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
            print(temp.data,end='    ')
            temp=temp.next
        print("end of Stack")

    def pop(self):
        if self.top is None:
            return -1
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self,value):
        if self.size()>=self.maxsize:
            print("stack overflow") 
            return
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
    def size(self):
        temp = self.top
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def undo_redo(self):
        st='uurru'
        name=Stack(self.maxsize)
        for char in st:
            if char=="u":
                val=self.pop()
                name.push(val)
            elif char=='r':
                val=name.pop()
                self.push(val)
    
n=Stack(7)
n.push('h')
n.push('e')
n.push('l')
n.push('l')
n.push('o')
n.push('h')
n.push('i')
n.undo_redo()
n.travesal()