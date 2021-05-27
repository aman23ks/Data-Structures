q = [4, 3, 1, 10, 2, 6]


def reverse(q):

    if q == []:
        return

    val = q.pop(0)

    if q != []:
        q = reverse(q)

    q = put_rev(q, val)

    return q


def put_rev(q, val):
    q.append(val)
    return q


print(reverse(q))
