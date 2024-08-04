class node():
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class doubly_ll():
    def __init__(self) :
        self.head = None
    
    def print_for(self):
        if self.head == None:
            print("List is empty")
        else:
            n=self.head
            while n is not None:
                print(f"{n.data}->",end="")
                n=n.nref
    
    def print_rev(self):
        print()
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



d=doubly_ll()
d.insert_end(12)
d.insert_end(15)
d.insert_after(45,12)
d.insert_before(78,12)
d.print_for()
d.print_rev()