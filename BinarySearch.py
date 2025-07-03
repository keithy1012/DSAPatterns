arr = [1,2,3,4,5,6,7,8]

def binarySearch(arr, target):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1

print(binarySearch(arr, 4))
print(binarySearch(arr, -1))