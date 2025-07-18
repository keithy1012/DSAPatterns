'''
From the numbers between [1,n], return all possible combinations of k numbers. 
'''
def combinations(n, k):
    res = []
    def backtrack(start, curr):
        if len(curr) == k:
            res.append(curr.copy())
        else:
            for ind in range(start, n+1):
                curr.append(ind)
                backtrack(ind+1, curr)
                curr.pop()
    backtrack(1, [])
    return res

print(combinations(4,2))
    