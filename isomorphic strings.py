s = "badc"
t = "baba"


def check(s, t):
    if len(s) != len(t):
        return False

    mydict = dict()
    val = ""

    for i in range(len(s)):
        if s[i] not in mydict:
            if t[i] not in val:
                mydict[s[i]] = t[i]
                val += t[i]
            else:
                return False

        else:
            if mydict[s[i]] != t[i]:
                return False

    return True


print(check(s, t))
