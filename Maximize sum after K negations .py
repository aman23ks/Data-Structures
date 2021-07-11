# N = 10
# K = 5
# arr = [5, -2, 5, -4, 5, -12, 5, 5, 5, 20]

arr = [3, 2, 1, 4, 5]
K = 5
N = 5


def maximizeSum(a, n, k):
    a.sort()

    count = 0
    for i in range(n):
        if a[i] < 0 and k > 0:
            a[i] = -a[i]
            k -= 1
        else:
            continue

    if k == 0:
        val = sum(a)
    else:
        a.sort()
        if (k-count) % 2 == 0:
            val = sum(a)
        else:
            a[0] = -a[0]
            val = sum(a)

    return val
