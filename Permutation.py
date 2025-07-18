'''
Given a list of distinct integers, generate a list of all permutations'''

def permutation(arr):
    res = []
    visited = [False] * len(arr)

    def backtracking(curr):
        if len(curr) == len(arr):
            res.append(curr.copy())
            return 
        for i in range(len(arr)):
            if visited[i] == False:
                visited[i] = True
                curr.append(arr[i])
                backtracking(curr)
                visited[i] = False
                curr.pop()
    backtracking([])
    return res

print(permutation([1,2,3]))