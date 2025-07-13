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

    def pop(self):
        if self.top==None:
            return -1
        else:
            data=self.top.data
            self.top=self.top.next
            print("book removed is:",data)
    def push(self,value):
        if self.size()>=self.maxsize:
            print("stack overflow") 
            return
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
    def size(self):
        temp=self.top
        count=0
        while temp is not None:
            temp=temp.next
            count+=1  
def menu():
        book=Stack(5)
        i=int(input("enter the number:"))
        while(True):
            if i == 1:
                value = input("Enter the book name to push: ")
                book.push(value)
                return
            elif i == 2:
                book.pop()
                return
            elif i == 3:
                print("Max size of stack:", book.maxsize)
                return
            elif i == 4:
                print("Current size of stack:", book.size())
                return
            elif i == 5:
                book.traversal()
                return
            elif i == 6:
                print("Exiting...")
                break
            # else:
            #     print("Enter a valid option (1–6)")
menu()