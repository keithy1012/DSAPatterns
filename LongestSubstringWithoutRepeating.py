
def longestWithoutRep(str):
    if len(str) == 0:
        return str

    l, r = 0, 1
    chars = []
    maxLength = 0
    while r < len(str):
        if str[r] not in chars:
            chars += str[r]
            maxLength = max(maxLength, len(chars)) 
        else:
            maxLength = max(maxLength, len(chars))
            while chars and str[r] in chars:
                chars.pop(0)
            chars += str[r]
        r += 1
            
    return maxLength

print(longestWithoutRep("abcdefghd"))