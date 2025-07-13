class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
        

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.value,end=' -> ')
            temp=temp.next
        print("None")
    def insert_start(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        if self.tail is None:
            self.tail=new_node    
    def update(self,index,data):
        new_node=Node(data)
        temp=self.head
        if index<0:
            return -1
        if index==0:
            self.insert_start(data)
        for i in range(index-1):
            temp=temp.next
        new_node.next=temp.next.next
        temp.next=new_node
    def insert_end(self,data):   
            new_node=Node(data)
            if not self.head:
                self.head=new_node
                self.tail=new_node
            self.tail.next=new_node
            self.tail=new_node

    #first occurance (all occurance karna hai)
    def delete(self,data):
        new_node=Node(data)
        temp=self.head 
        if temp is None:
                print("empty")
                return
        if temp.value==data:
                self.head=temp.next
                if self.head==None:
                    self.tail=None
                return
        while temp!=None:
            temp=temp.next
            if temp.next.value==data:
                temp.next=temp.next.next
                return
    def delete_at_index(self,index):
         temp=self.head
         if index<0:
              print("chal chal")   
         if index==0:
            self.head=temp.next
            if self.head==None:
                    self.tail=None
            return
         for i in range(index-1):
            temp=temp.next
            if temp.next==None:
                 print("out of bound")
                 return
         temp.next=temp.next.next
    
    def middle(self):
         slow=self.head
         fast=self.head
         while fast and fast.next!=None:
              slow=slow.next
              fast=fast.next.next

         print(slow.value)
                   
    def reverse(self):
         prev=None
         curr=self.head
         
         while curr:
              temp=curr.next
              curr.next=prev
              prev=curr
              curr=temp
         return prev
              
    def  rotate_at(self,index):
         temp=self.head
         org=self.head
         for i in range(index):
              temp=temp.next
         self.head=temp
         self.tail.next=org
         


                          
       


ll=linkedlist()
ll.insert_end(5)
ll.insert_end(3)
ll.insert_end(5)
ll.insert_end(2)
ll.insert_end(2)
ll.insert_end(3)
ll.display()
ll.rotate_at(4)
# ll.middle()
ll.display()
# temp=ll.reverse()
# while temp:
#      print(temp.value,end=' -> ')
#      temp=temp.next
# print('None')

# ll.display()
# # ll.delete(5)
# ll.delete_at_index(1
#                    )

 
