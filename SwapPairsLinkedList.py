class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.n = n
first = Node(0)
first.n = Node(5)
first.n.n = Node(9)
first.n.n.n = Node(13)

'''
Two cases of even/odd nodes: 1->2 or 1->2->3
Assume we have 2 pointers: first and second. 
dummy -> 1 -> 2 -> 3
first = dummy.next = 1
second = dummy.next.next = 2
prev = dummy
algo:
while second:
1. temp = second.next
2. second.next = first
3. first.next = temp
4. prev.next = second
5. prev = first
6. first = temp
7. if temp.next: second = temp.next, else: second = None
'''
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
