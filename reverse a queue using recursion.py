q = [4, 3, 1, 10, 2, 6]

# add code here


def reverse(q):

    if q == []:
        return

    val = q.pop(0)

    q = q[1:]

    reverse(q)

    put_rev(q, val)

    return q


def put_rev(q, val):

    if q == []:
        q.append(val)
    return


print(reverse(q))
