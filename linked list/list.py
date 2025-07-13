class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

item1=Node(5)
item2=Node(4)        
item3=Node(8)
item4=Node(1)
item1.next=item2
item2.next=item3
item3.next=item4


print(item1.next.next)
print(item3)

