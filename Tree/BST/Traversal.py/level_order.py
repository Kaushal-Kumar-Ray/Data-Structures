from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

def levelorder(root):
    if not root:
        return
    queue=deque()
    queue.append(root)
    while queue:
        current=queue.popleft()
        print(current.data,end=' ')
        if current.leftchild:
            queue.append(current.leftchild)
        if current.rightchild:
            queue.append(current.rightchild)
  
        
root=TreeNode('N1')
root.leftchild=TreeNode('N2')
root.rightchild=TreeNode('n3')
root.leftchild.leftchild=TreeNode('N4')
root.leftchild.rightchild=TreeNode('N5')

print("Level Order traversal")
levelorder(root)