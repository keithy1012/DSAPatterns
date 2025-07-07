def generateParentheses(n):
    def helper(open_count, close_count, curr):
        if open_count == n:
            while close_count < n:
                curr += ")"
                close_count += 1
            return [curr]
        if open_count == close_count: 
            return helper(open_count+1, close_count, curr + "(")
        # more open than close
        else:
            return helper(open_count+1, close_count, curr+"(") + helper(open_count, close_count+1, curr+")")
    return helper(0, 0, "")

print(generateParentheses(3))