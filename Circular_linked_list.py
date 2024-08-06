# Circular Singly Linked List

class node():
    def __init__(self,data):
        self.data = data
        self.ref = None

class Circular_ll():
    def __init__(self):
        self.head = None
    def insert_beg(self,x):
        new_node = node(x)
        if self.head is None:
            self.head = new_node
            new_node.ref = self.head
        else:
            n = self.head
            while n.ref is not self.head:
                n = n.ref
            n.ref = new_node
            new_node.ref = self.head
            self.head = new_node

    def insert_end(self,x):
        new_node = node(x)
        if self.head is None:
            self.head = new_node
            new_node.ref = self.head
        else:
            n = self.head
            while n.ref is not self.head:
                n = n.ref
            n.ref = new_node
            new_node.ref = self.head

    def insert_mid(self,x,pos):
        new_node = node(x)
        if self.head is None:
            print("LL is empty, so inserting in 0th position")
            self.head = new_node
            new_node.ref = self.head
        if pos == 0:
            self.insert_beg(x)
            return
        else:
            n = self.head
            for i in range(pos-1):
                n = n.ref
            if n.ref:
                new_node.ref = n.ref
                n.ref = new_node

    def del_beg(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            n = self.head
            while n.ref is not self.head:
                n = n.ref
            self.head = self.head.ref
            n.ref = self.head

    def del_end(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            n = self.head
            while n.ref.ref is not self.head:
                n = n.ref
            n.ref = self.head

    def del_by_value(self,v):
        if self.head is None:
            print("list is empty")
            return
        if self.head.data == v:
            self.del_beg()
        else:
            n = self.head
            while n.ref is not self.head:
                if v == n.ref.data:
                    break
                n =n.ref
            if v == n.ref.data:
                n.ref = n.ref.ref
            else:
                print("Value not found")

    def print_ll(self):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        while n.ref is not self.head:
            print(f"{n.data}->",end='')
            n = n.ref
        print(n.data)

    def insert(self):
        c = int(input("\n1.At begin \n2.At End \n3.At position\n"))
        x = int(input("Enter the value: "))
        if c == 1:
            self.insert_beg(x)
            return
        elif c == 2:
            self.insert_end(x)
            return
        elif c == 3:
            pos = int(input("Enter the position: "))
            self.insert_mid(x,pos)
            return
        else:
            print("Wrong choice")
            return
        
    def delete(self):
        c = int(input("\n1.At begin \n2.At End \n3.By value\n"))
        if c == 1:
            self.del_beg()
            return
        elif c == 2:
            self.del_end(x)
            return
        elif c == 3:
            pos = int(input("Enter the Value: "))
            self.del_by_value(pos)
            return
        else:
            print("Wrong choice")
            return



l=Circular_ll()

while True:
    ch = int(input("\n1.Insertion \n2.Deletion \n3.Display \n4.Exit\n"))
    if ch == 1:
        l.insert()
    if ch == 2:
        l.delete()
    if ch == 3:
        l.print_ll()
    if ch == 4:
        break

# l.insert_beg(20)
# l.insert_beg(30)
# l.insert_beg(40)
# l.insert_beg(50)
# l.insert_end(60)
# l.insert_end(70)
# # l.insert_mid(111,0)
# l.print_ll()
# # l.del_beg()
# l.del_by_value(50)
# # l.del_end()
# l.print_ll()
