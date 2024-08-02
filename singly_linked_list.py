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
    
    def del_beg(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head=self.head.ref

    def del_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def del_val(self):
        if self.head is None:
            print("List is empty")
            return
        x=int(input("Enter the value to be deleted: "))
        if x == self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Element not found")
        else:
            n.ref=n.ref.ref
    
    def delete(self):
        if self.head is None:
            print("List is empty")
            return
        c=int(input("\nWhere do you want to perform deletion:\n1.At beginning\n2.At end\n3.delete a specific value\n"))
        if c == 1:
            self.del_beg()
        elif c == 2:
             self.del_end()
        elif c == 3:
            self.del_val()
        else:
            print("Wrong choice!")

    def insert(self):
        ch=int(input("\nWhat operation? \n1.Insert at beginnig\n2.Insert at end\n3.insert at position\n4.display\n"))
        if ch ==1:
            num=int(input("Enter the number: "))
            ll.add_begin(num)
        elif ch ==2:
            num=int(input("Enter the number: "))
            ll.add_end(num)
        elif ch ==3:
            num=int(input("Enter the number: "))
            ll.add_pos(num)
        else:
            print("Wrong choice!")




ll=linkedList()
while True:
    ch=int(input("\nWhat operation? \n1.Insertion\n2.Deletion\n3.Display\n4.Exit\n"))
    if ch ==1:
        ll.insert()
    if ch ==2:
        ll.delete()
    if ch ==3:
        ll.print_LL()
    if ch==4:
        break
