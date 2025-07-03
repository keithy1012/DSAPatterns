class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.n = n
first = Node(0)
first.n = Node(5)
first.n.n = Node(9)

second = Node(-1)
second.n = Node(6)
second.n.n = Node(8)
second.n.n.n = Node(9)

def mergeLL(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    head = Node()
    dummy = head
    while l1 and l2:
        if l1.val < l2.val:
            dummy.n = Node(l1.val)
            l1 = l1.n
            dummy = dummy.n
        else:
            dummy.n = Node(l2.val)
            l2 = l2.n
            dummy = dummy.n
    dummy.n = l1 if l1 else l2
    return head.n

merged = mergeLL(first, second)


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.n

print_list(merged)