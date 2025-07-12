class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.n = n
first = Node(0)
first.n = Node(0)
first.n.n = Node(5)
first.n.n.n = Node(9)
first.n.n.n.n = Node(9)
first.n.n.n.n.n = Node(13)

def RemoveAllDuplicates(head):
    if head is None or head.n is None:
        return head
    dummy = Node(0, head)
    prev = dummy
    curr = head
    while curr and curr.n:
        if curr and curr.val == curr.n.val:
            dup_value = curr.val
            while curr and curr.val == dup_value:
                curr = curr.n
            prev.n = curr
        prev = curr
        curr = curr.n
    return dummy.n


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.n

new = RemoveAllDuplicates(first)
print_list(new)
