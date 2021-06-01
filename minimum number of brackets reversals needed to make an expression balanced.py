def countRev(s):
    if len(s) % 2 != 0:
        return -1

    arr = []
    c = 0
    c1 = 0
    for i in s:
        if i == "{":
            arr.append(i)
            c1 += 1
            # print(i,c1,arr)
        elif i == "}" and arr != [] and arr[-1] == "{":
            # print(arr)
            arr = arr[:-1]
            # print(arr)
            c1 -= 1
        else:
            c += 1
            # print(i,c)

    # print(c, c1)
    if c % 2 == 0:
        c = c//2
    else:
        c = c//2 + 1

    if c1 % 2 == 0:
        c1 = c1//2
    else:
        c1 = c1//2 + 1

    return c+c1


print(countRev("{}{{}{{{{{}}{}"))
