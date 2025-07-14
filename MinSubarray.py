# Kadane's Algorithm 
'''
At every number we have 2 options:
    1. Add this number to our subsequence
    2. Start a new subsequence from this num
'''

def minSubarray(arr):
    curr_min = arr[0]
    global_min = arr[0]

    for i in range(1, len(arr)):
        curr_min = min(arr[i], curr_min + arr[i])
        global_min = min(global_min, curr_min)
    return global_min

print(minSubarray([1,-2, -3, 2,3]))