class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.n = n
first = Node(0)
first.n = Node(5)
first.n.n = Node(9)
first.n.n.n = Node(13)

'''
If we wanted to remove the 3rd node from the end, and we have a total of 5 nodes:
1->2->3->4->5 (we want to remove 3) => that node is 5-3=2 nodes from the start.
'''
def removeNthNodeFromEnd(head, n):
    dummy = head
    numNodes = 0
    while dummy:
        numNodes += 1
        dummy = dummy.n
    nth_from_start = numNodes - n
    print(nth_from_start)
    new_start = head
    for ind in range(nth_from_start-1):
        new_start = new_start.n
    new_start.n = new_start.n.n
    return head

removed = removeNthNodeFromEnd(first, 2)

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.n

print_list(removed)