def longestPrefix(strs):

    if not strs:
        return False

    for i in range(len(strs[0])):
        ch = strs[0][i]

        for word in strs:
            if i >= len(word) or word[i]!=ch:
                return strs[0][:i]

    return strs[0]

strs = ["apple","app","applicable"]
print("common prefix = ", longestPrefix(strs))

    