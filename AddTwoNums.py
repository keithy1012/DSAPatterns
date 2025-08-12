class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.n = n
# 1 -> 2 -> 3
first = Node(1)
first.n = Node(2)
first.n.n = Node(3)

# 2 -> 8 -> 9
second = Node(2)
second.n = Node(8)
second.n.n = Node(9)

def addTwoNums(l1, l2):
    carryOver = 0
    res = Node()
    dummy = res
    while l1 or l2:
        dummy.n = Node()
        dummy = dummy.n
        if l1 and l2:
            val = l1.val + l2.val + carryOver
        elif l1:
            val = l1.val + carryOver
        else:
            val = l2.val + carryOver
        carryOver = 0
        if val >= 10:
            val -= 10
            carryOver = 1
        dummy.val = val
        if l1:
            l1 = l1.n
        if l2:
            l2 = l2.n
    if carryOver:
        dummy.n = Node(1)
        
    return res.n

def printList(ll):
    while ll:
        print(ll.val, end="->")
        ll=ll.n
print(printList(addTwoNums(first, second)))