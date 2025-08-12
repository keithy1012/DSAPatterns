
def searchRotated(arr, target):
    l, r = 0, len(arr)-1
    while l < r: 
        mid = (l+r)//2
        if target == arr[mid]:
            return mid
        # if the left portion is sorted
        if arr[l] <= arr[mid]:
            if arr[l] <= target < arr[mid]:
                r = mid-1
            else:
                l = mid + 1
        # right portion is sorted
        else:
            if arr[mid] < target < arr[r]:
                l = mid+1
            else:
                r = mid-1
    return -1

print(searchRotated([5,6,1,2,3,4], 3))


