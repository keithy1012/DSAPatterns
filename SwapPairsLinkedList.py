class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.n = n
first = Node(0)
first.n = Node(5)
first.n.n = Node(9)
first.n.n.n = Node(13)


def swapPairs(head):
    if head is None or head.n is None:
        return head
    dummy = Node(0, head)
    prev = dummy
    first = dummy.n
    second = dummy.n.n

    while second:
        temp = second.n
        prev.n = second
        second.n = first
        first.n = temp
        prev = first
        first = first.n
        if temp:
            second = temp.n
        else:
            break

    return dummy.n


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.n

new = swapPairs(first)
print_list(new)
