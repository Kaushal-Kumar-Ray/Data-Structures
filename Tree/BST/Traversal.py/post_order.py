class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

def postorder(root):
    if root:
        postorder(root.leftchild)
        postorder(root.rightchild)
        print(root.data,end=' ')
        
root=TreeNode('N1')
root.leftchild=TreeNode('N2')
root.rightchild=TreeNode('n3')
root.leftchild.leftchild=TreeNode('N4')
root.leftchild.rightchild=TreeNode('N5')

print("Post Order traversal")
postorder(root)