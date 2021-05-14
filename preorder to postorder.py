pre = [40, 30, 32, 35, 80, 90, 100, 120]
size = len(pre)

arr = []


def build_tree(pre, l, r):
    if l > r:
        return None
    root = pre[l]

    idx = l+1
    while idx < r and pre[l] > pre[idx]:
        idx += 1

    build_tree(pre, l+1, idx-1)
    build_tree(pre, idx, r)

    arr.append(root)


build_tree(pre, 0, size-1)
print(arr)
