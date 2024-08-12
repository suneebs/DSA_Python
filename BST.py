class BST():
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key == None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else: 
                self.rchild  = BST(data)
root = BST(10)
root.lchild = BST(5)
root.insert(20)

print(root.key)
print(root.lchild)
print(root.rchild)
print(root.lchild.key)
print(root.lchild.lchild)
print(root.lchild.rchild)