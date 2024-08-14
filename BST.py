class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        # Checking Root node
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

    #  Search
    def search(self,data):
        if self.key == data :
            print("Node is found!")
            return
        if data < self.key :
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not found!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node not found")
    
    # PreOrder
    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    #inorder
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

    #postorder
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")

        
root = BST(None)
# root.lchild = BST(5)
# root.insert(20)
list = [10,6,3,1,6,98,3,7]
for i in list:
    root.insert(i)
root.search(1)
print("PreOrder:")
root.preorder()
print("\nInOrder:")
root.inorder()
print("\nPostOrder:")
root.postorder()
# print(root.key)
# print(root.lchild)
# print(root.rchild)
# print(root.lchild.key)
# print(root.lchild.lchild)
# print(root.lchild.rchild)