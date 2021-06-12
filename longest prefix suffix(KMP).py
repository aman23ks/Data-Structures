def LongestPrefixSuffix(s):
    i = 0
    j = 1
    n = len(s)
    lps = [0]
    while j < n:
        if s[i] == s[j]:
            lps.append(i+1)
            j += 1
            i += 1
        else:
            if i == 0:
                lps.append(0)
                j += 1
            else:
                i = lps[i - 1]

    return lps[n-1]


print(LongestPrefixSuffix("ababab"))
