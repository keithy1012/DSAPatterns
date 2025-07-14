'''
Implementation of Kadane's

1. Find both min and max subarrays and total value of array
2. If total < 0: return max_subarray (since all values are negative, we return the "smallest" negative num)
3. Else: return the max(max_subarray, total - min_subarray) --> total-minsubarray accounts for "wrapping" around array
'''

def maxInCircularArray(nums):
    total = nums[0]
    curr_min = global_min = curr_max = global_max = nums[0]

    for i in range(1, len(nums)):
        total += nums[i]
        curr_min = min(nums[i], curr_min + nums[i])
        curr_max = max(nums[i], curr_min + nums[i])
        global_min = min(global_min, curr_min)
        global_max = max(global_max, curr_max)
    
    if total < 0:
        return global_max
    else:
        return max(total - global_min, global_max)

print(maxInCircularArray([5, -3, 5]))