def sort_stack(s):
    if s == []:
        return []

    temp = s[-1]
    s = s[:-1]
    s = sort_stack(s)

    s = put_sorted(s, temp)

    return s


def put_sorted(s, temp):

    if s == []:
        s.append(temp)
        return s

    val = s[-1]

    s = s[:-1]
    s = put_sorted(s, temp)
    s.append(val)
    return s


print(sort_stack([11, 2, 32, 3, 41]))
