arr = [4,2,3,8]

def sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = sort(arr[:mid])
    right = sort(arr[mid:])
    res = merge(left, right)
    return res


def merge(l1, l2):
    res = []
    l1p = l2p = 0
    while l1p < len(l1) and l2p < len(l2):
        if l1[l1p] < l2[l2p]:
            res.append(l1[l1p])
            l1p += 1
        else:
            res.append(l2[l2p])
            l2p += 1
    while l1p < len(l1):
        res.append(l1[l1p])
        l1p += 1
    while l2p < len(l2):
        res.append(l2[l2p])
        l2p += 1
    return res

print(sort(arr))