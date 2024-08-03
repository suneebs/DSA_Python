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
                print(f"{n.data}->")
                n=n.nref
    
    def print_rev(self):
        if self.head is None:
            print("List is empty")
        else:
            n=self.head
            while n.nref is not None:
                n = n.ref
            while n is not None:
                print("s{n.data}->")
                n=n.pref

d=doubly_ll()
d.print_for()
d.print_rev()