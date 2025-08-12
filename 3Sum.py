
def threesum(arr, target):
    res = []
    for ind in range(0, len(arr)-2):
        remaining = target - arr[ind]
        l, r = ind + 1, len(arr)-1
        while l < r:
            mid = (l + r) // 2
            if arr[l] + arr[r] == remaining:
                res.append([arr[ind], arr[l], arr[r]])
                break
            elif arr[l] + arr[r] > remaining:
                r = mid - 1
            else:
                l = mid + 1

    return res

print(threesum([1,2,3,3,4,5,6,6], 12))