class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
    
def preorder(root):
        if root:
            print(root.data,end=' ')
            preorder(root.leftchild)
            preorder(root.rightchild)
           
root=TreeNode('N1')
root.leftchild=TreeNode('N2')
root.rightchild=TreeNode('N3')
root.leftchild.leftchild=TreeNode('N4')
root.leftchild.rightchild=TreeNode('N5')

print("Pre Order Traaversal")
preorder(root)