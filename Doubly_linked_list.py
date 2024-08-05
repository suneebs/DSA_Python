class node():
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class doubly_ll():
    def __init__(self) :
        self.head = None
    
    def print_for(self):
        print("forward:",end='')
        if self.head == None:
            print("List is empty")
        else:
            n=self.head
            while n is not None:
                print(f"{n.data}->",end="")
                n=n.nref
    
    def print_rev(self):
        print("\nreverse:",end='')
        if self.head is None:
            print("List is empty")
        else:
            n=self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(f"{n.data}->", end="")
                n=n.pref

    def insert_beg(self,data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def insert_end(self,data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref = new_node
            new_node.pref = n
    
    def insert_after(self,data,x):
        if self.head is None:
            print("\nList is empty")
            return
        new_node = node(data)
        n=self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if x is n.data:
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node
        else:
            print("Given node is not in the list")

    def insert_before(self,data,x):
        if self.head is None:
            print("\nList is empty")
            return
        new_node = node(data)
        n=self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if x is n.data:
            new_node.nref = n
            new_node.pref = n.pref
            if n.pref is not None:
                n.pref.nref = new_node
            else:
                self.head = new_node
            n.pref = new_node
        else:
            print("Given node is not in the list ")

    def del_beg(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.nref is None:
            self.head = None
        else:
            self.head = self.head.nref
            self.head.pref = None

    def del_end(self):
        if self.head is None:
            print("Linked list is empyty")
            return
        if self.head.nref is None:
            self.head = None
        else:
            n = self.head 
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def del_by_value(self,x):
        if self.head is None:
            print("Linked list is empyty")
            return
        elif self.head.nref is None:
            self.head = None
            return
        elif x is self.head.data:
            self.head = self.head.nref
            self.head.pref = None
        else:
            n = self.head.nref
            while n.nref is not None:
                if x == n.data:
                    break
                else:
                    n=n.nref
            if n.nref is not None:
                n.nref.pref = n.pref
                n.pref.nref = n.nref
            else:
                if n.data == x:
                    n.pref.nref = None
                else:
                    print("\nValue is not present in the LL")
    def insertion(self):
        n = int(input("Enter the number: "))
        c = int(input("Where do you want to insert? \n1.Beginnig \n2.End \n3.After/before a cerain node\n"))
        if c == 1:
            self.insert_beg(n)
        elif c == 2:
            self.insert_end(n)
        elif c == 3:
            no = int(input("Select the node: "))
            s = int(input("Where do you want to insert? \n1.After the node \n2.Before the node: "))
            if s == 1:
                self.insert_after(n,no)
            elif s == 2:
                self.insert_before(n,no)
            else:
                print("Wrong choice")
        else:
            print("Wrong choice")

    def deletion(self):
        c = int(input("Where do you want to delete? \n1.Beginnig \n2.End \n3.By value\n"))
        if c == 1:
            self.del_beg()
        elif c == 2:
            self.del_end()
        elif c == 3:
            no = int(input("Enter the number to be deleted: "))
            self.del_by_value(no)
        else:
            print("Wrong choice")      

   

d=doubly_ll()

while True:
    ch = int(input("\n1.Insertion \n2.Deletion \n3.Display \n4.Exit\n"))
    if ch == 1:
        d.insertion()
    elif ch == 2:
        d.deletion()
    elif ch == 3:
        d.print_for()
        d.print_rev()
    elif ch == 4:
        break
    else:
        print("\nEnter correct option")
# d.insert_end(12)
# d.insert_end(15)
# d.insert_after(45,12)
# d.insert_before(78,12)
# d.print_for()
# d.del_by_value(34)
# d.print_for()
# d.print_rev()