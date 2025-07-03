class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.n = n
three = Node(3)
two = Node(2, three)
one = Node(1, two)
root = Node(0, one)

def reverseLL(root):
    prev = None

    while root:
        temp = root.n
        root.n = prev
        prev = root
        root = temp
    return prev

new = reverseLL(root)


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.n

print_list(new)
print("")