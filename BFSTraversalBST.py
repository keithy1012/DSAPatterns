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
root = generate_bst()
'''
    4
  2   6
1  3 5 7
'''

def bfs_traversal(root):
    if root is None:
        return root
    res = []
    queue = []
    queue.append(root)
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            res.append(node.val)
    return res

def bfs_traversal_in_levels(root):
    queue = []
    queue.append(root)
    res = []
    while queue:
        level_length = len(queue)
        level = []
        for i in range(level_length):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level.append(node.val)
        res.append(level)
    return res
        
print(bfs_traversal(root))
print(bfs_traversal_in_levels(root))
