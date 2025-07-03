class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.n = n
three = Node(3)
two = Node(2, three)
one = Node(1, two)
root = Node(0, one)

def splitLL(root):
    dummy = root
    prev = None
    slow = root
    fast = root
    while fast and fast.n:
        prev = slow
        slow = slow.n
        fast = fast.n.n
    prev.n = None
    return dummy, slow
first, second = splitLL(root)

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.n

print_list(first)
print("")
print_list(second)