def sort_stack(s):
    if s == []:
        return 0

    temp = s[-1]
    s = s[:-1]
    sort_stack(s)

    put_sorted(s, temp)

    return s


def put_sorted(s, temp):

    # print(s)
    if s == [] or temp < s[-1]:
        s.append(temp)
        print(s)
        return 0

    val = s[-1]
    print(val)

    s = s[:-1]
    print(s)
    put_sorted(s, temp)
    print(s)
    s.append(val)
    print(s)
    return 0


print(sort_stack([11, 2, 32, 3, 41]))
