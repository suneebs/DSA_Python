class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


class linkedList:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print("List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"->",end='')
                n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.ref is not None:
                temp=temp.ref
                
            temp.ref=new_node

    def add_pos(self,data):
        pos= int(input("Enter the position: "))
        if pos==0:
            self.add_begin(data)
            return
        temp=self.head
        if temp == None:
            print("List is empty")
            return
        i=1
        while temp.ref is not None:
            i+=1
            temp=temp.ref
        if pos>i:
            print("position exceeded")
            return

        temp=self.head
        for i in range(pos-1):
            temp=temp.ref
            print(temp.data)
        new_node=Node(data)
        new_node.ref=temp.ref
        temp.ref=new_node 




ll=linkedList()
while True:
    ch=int(input("\nWhat operation? \n1.Insert at beginnig\n2.Insert at end\n3.insert at position\n4.display\n"))
    if ch ==1:
        num=int(input("Enter the number: "))
        ll.add_begin(num)
    if ch ==2:
        num=int(input("Enter the number: "))
        ll.add_end(num)
    if ch ==3:
        num=int(input("Enter the number: "))
        ll.add_pos(num)
    if ch==4:
        ll.print_LL()
    if ch==5:
        break



# ll.add_begin(20)
# ll.add_end(30)
# ll.add_pos(40)
# ll.print_LL()

