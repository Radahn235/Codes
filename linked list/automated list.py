class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_end(self,data):   
            new_node=Node(data)
            if not self.head:
                self.head=new_node
                self.tail=new_node
            self.tail.next=new_node
            self.tail=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.val,end=' -> ')
            temp=temp.next
        print("None")
    def insert_start(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        if self.tail is None:
            self.tail=new_node
    def insert_between(self,index,data):
        new_node=Node(data)
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
    def insert_at_pos(self,index,data):
        if index<0:
            print("anda hai kya l")
            return
        if index==0:
            self.insert_start(data)
        new_node=Node(data)
        temp=self.head
        for i in range(index-1):
            if (temp.next==None):
                print("index out of bound")


ll =linkedlist()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_start(50)
ll.insert_between(1,69)
ll.insert_at_pos(2 ,55)

ll.display()

