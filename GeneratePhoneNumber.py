def generateNumber(digits):
    def helper(remaining_digs, curr):
        if len(remaining_digs) == 0:
            return curr
        else:
            temp = []
            keyboard = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"
                }
            letters = keyboard.get(str(remaining_digs[0]))
            for number in curr:
                for letter in letters:
                    temp.append(number+letter)
            return helper(remaining_digs[1:], temp)
                
    res = []
    if len(digits) == 0:
        return res
        
    res += [""]
    return helper(digits, res)

print(generateNumber("23"))