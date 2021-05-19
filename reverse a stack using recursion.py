s = [1, 2, 3, 4]


def sort(s):
    if s == []:
        return

    val = s[-1]
    s = s[:-1]

    sort(s)

    add_to_stack(s, val)

    return s


def add_to_stack(s1, val):

    if s1 == []:
        s1.append(val)
        return

    temp = s1[-1]

    s1 = s1[:-1]

    add_to_stack(s1, val)

    s1.append(temp)

    return


print(sort(s))
