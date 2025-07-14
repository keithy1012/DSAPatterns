# Kadane's Algorithm
'''
At every number we have 2 options:
    1. Add this number to our subsequence
    2. Start a new subsequence from this num
'''
def maxSubarray(arr):
    currSum = float("-inf")
    maxSum = float("-inf")
    for num in arr:
        currSum = max(num, currSum + num)
        maxSum = max(maxSum, currSum)
    return maxSum

print(maxSubarray([1,2,-4, 3]))