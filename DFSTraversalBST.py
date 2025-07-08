class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_bst():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    return root
'''
    4
  2   6
1  3 5 7
'''
def preorder(root):
    if root is None:
        return []
    res = [root.val] + preorder(root.left) + preorder(root.right)
    return res

def inorder(root):
    if root is None:
        return []
    res = inorder(root.left) + [root.val] + inorder(root.right)
    return res

def postorder(root):
    if root is None:
        return []
    res = postorder(root.left) + postorder(root.right) + [root.val]
    return res
root = generate_bst()
print(preorder(root))
print(inorder(root))
print(postorder(root))