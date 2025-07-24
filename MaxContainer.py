
def maxContainerArea(heights):
    if len(heights) <= 1:
        return 0
    l, r = 0, len(heights)-1
    maxArea = 0
    while l < r:
        temp_area = (r - l) * min(heights[l], heights[r])
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
        maxArea = max(maxArea, temp_area)
    return maxArea

print(maxContainerArea([1,8,6,2,5,4,8,3,7]))