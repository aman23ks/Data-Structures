strs = ["flower", "flow", "flight"]


def longestCommonPrefix(strs):
    if not strs:
        return ""
    minLen = len(strs[0])
    for i in range(1, len(strs)):
        minLen = min(minLen, len(strs[i]))

    lcp = ""
    i = 0

    while i < minLen:
        char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != char:
                return lcp
        lcp += char
        i += 1

    return lcp


print(longestCommonPrefix(strs))
