s = "0100110101"


def substring(s):

    x, y, c = 0, 0, 0

    for i in s:
        if i == "0":
            x += 1
        else:
            y += 1

        if x == y:
            c += 1

    return c


print(substring(s))
