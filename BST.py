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

    #delete
    def delete(self,val,curr):
        if self.key is None:
            print("Tree is empty")
            return
        if val < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(val,curr)
            else:
                print(f"{val} is not present in the tree")

        elif val > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(val,curr)
            else:
                print(f"{val} is not present in the tree")

        else:
            if self.lchild is None:
                temp = self.rchild
                if curr == val:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp =None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if curr == val:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp =None
                    return
                self = None
                return temp
            else:
                node = self.rchild
                while node.lchild:
                    node = node.lchild
                self.key = node.key
                self.rchild = self.rchild.delete(node.key,curr)

        return(self)
    
    #min and max value in the tree
    def min(self,root):
        node =root
        if node.lchild:
            self.min(node.lchild)
        else:
            print("\nmin: ",node.key) 
    # def min(self):
    #     node = self
    #     while node.lchild:
    #         node = node.lchild
    #     print("\nMin: ",node.key)  

    def max(self):
        node = self
        while node.rchild:
            node = node.rchild
        print("Max: ",node.key) 

   
# counting number of nodes

def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)

###########################################################################
root = BST(None)
# root.lchild = BST(5)
# root.insert(20)
list = [10,6,3,1,6,98,3,7]
for i in list:
    root.insert(i)

###########################################################################
root.search(1)
print("PreOrder:",end=' ')
root.preorder()
print("\nInOrder:",end=' ')
root.inorder()
print("\nPostOrder:",end=' ')
root.postorder()
# print("\n",count(root))
if count(root) > 1:
    root.delete(10,root.key)
else:
    print("Cannot perform delete operation")
print()
root.preorder()
# print(root.key)
# print(root.lchild)
# print(root.rchild)
# print(root.lchild.key)
# print(root.lchild.lchild)
# print(root.lchild.rchild)
 
root.min(root)
root.max()