class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doubly:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=' <=> ')
            temp=temp.next
        print("None")    
    def display_back(self):
         temp=self.head
         if not temp:
              print("empty")
         while temp.next:
              temp=temp.next
         while temp:
              print(temp.data,end=' <=> ')
              temp=temp.prev
         print("None")

    def insert_end(self,data):
        new_node=Node(data)
        if not self.head:
                self.head=new_node
                return
        temp=self.head
        while temp.next:
             temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def insert_start(self,data):
        new_node=Node(data)
        if not self.head:
                self.head=new_node
                new_node.prev=None
                return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        new_node.prev=None
    def insert_between(self,index,data):
        new_node=Node(data)
        if index<0:
             print("ghar nikal")
             return
        if index==0:
             self.insert_start(data)
             return
        temp=self.head
        for i in range(index-1):
            temp=temp.next 
            if not temp:
                 print("out of bound")
                 return   
        new_node.next=temp.next
        temp.next=new_node
        new_node.prev=temp
        if new_node.next:
             new_node.next.prev = new_node
    def delete(self,value):
        new_node=Node(value)
        temp=self.head 
        if temp is None:
                print("empty")
                return
        while temp:
            if temp.data == value:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                     self.head=temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return 
            temp = temp.next 
    def delete_at(self,index):
         
        #  if index<0:
        #       print("nikal")
        #       return
        #  temp=self.head
        #  for i in range(index):
              
        #       if not temp:
        #          print("out of bound")
        #          return
        #       temp=temp.next
        #  if temp.prev:
        #              temp.prev.next=temp.next
        #  else:
        #              self.head=temp.next
        #  if temp.next:
        #              temp.next.prev=temp.prev
        temp=self.head
        if index<0:
             print("nikal")
             return
        if index==0:
             self.head=temp.next
             if self.head:
                  self.head.prev=None
             return
        for i in range(index):
             temp=temp.next
             if not temp:
                  print("index out of bound")
                  return 
        if temp.prev:
                     temp.prev.next=temp.next
        if temp.next:
                     temp.next.prev=temp.prev
    def palindrome(self):
        #  prev=None
        #  curr=self.head
        #  temp2={}
        #  while curr:
        #       temp=curr.next
        #       curr.next=prev
        #       prev=curr
        #       curr=temp
        #       return prev
        temp=self.head
        while temp.next:
             temp=temp.next
        temp1=self.head
        while temp1 != temp and temp1.prev != temp:
            if temp.data != temp1.data:
                print("Not a palindrome")
            return
        temp1 = temp1.next
        temp = temp.prev

        print("Palindrome")


        
dll=doubly()
dll.insert_end(1)
dll.insert_end(0)
dll.insert_end(4)
# dll.insert_end(3)
# dll.insert_end(2)
# dll.insert_end(1)
# dll.insert_between(7,7)
# dll.delete_at(7)
dll.palindrome()
dll.display()
dll.display_back()

