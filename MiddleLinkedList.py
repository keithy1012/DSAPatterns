class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.n = n
three = Node(3)
two = Node(2, three)
one = Node(1, two)
root = Node(0, one)

def findMiddle(root):
    if root is None or root.n is None:
        return root.val

    slow = root
    fast = root
    while fast and fast.n:
        slow = slow.n
        fast = fast.n.n
    
    return slow

mid = findMiddle(root)
print(mid.val)

