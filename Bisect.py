
arr = [0,1,3,3,3,4,5,5]
def Bisect_Left(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r)//2
        if arr[mid] >= target:
            r = mid
        else:
            l = mid+1
    return l


def Bisect_Right(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r)//2
        if arr[mid] <= target:
            l = mid+1
        else:
            r = mid

    return l