class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.n = n
first = Node(0)
first.n = Node(5)
first.n.n = Node(9)
first.n.n.n = Node(13)
first.n.n.n.n = first.n

second = Node(0)
second.n = Node(5)
second.n.n = Node(9)
second.n.n.n = Node(13)
def hasCycle(head):
    if head is None or head.n is None:
        return False
    slow = head
    fast = head.n

    while fast and fast.n:
        if slow == fast:
            return True
        slow = slow.n
        fast = fast.n.n
    return False

print(hasCycle(first))
print(hasCycle(second))