class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
    
def print_tree(node,level=0,prefix="Root:"):
    if node is not None:
        print(" "*(level*4)+prefix+str(node.data))
        print_tree(node.leftchild,level+1,"L----")
        print_tree(node.rightchild,level+1,"R----")
           
root=TreeNode('N1')
root.leftchild=TreeNode('N2')
root.rightchild=TreeNode('N3')
root.leftchild.leftchild=TreeNode('N4')
root.leftchild.rightchild=TreeNode('N5')

print("Pre Order Traaversal")
print_tree(root)