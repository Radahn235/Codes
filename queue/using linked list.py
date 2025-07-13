class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,value):
        new_node=Node(value)
        if self.front==None:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
    def traverse(self):
        temp=self.front
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.next
    def dequeue(self):
        if self.front==None:
            return print("line khali hai")
        self.front=self.front.next
    def is_empty(self):
        return self.front==None
    
    def first_last(self):
        if self.front==None:
            print("khali hai")
        else:
            print(self.front.data)
            print(self.rear.data)
q=Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.is_empty())
# q.dequeue()
# q.first_last()
# q.traverse()