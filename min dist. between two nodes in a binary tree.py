def lca(root, n1, n2):
    # Code here
    if not root:
        return None
    if root.data == n1 or root.data == n2:
        return root

    l = lca(root.left, n1, n2)
    r = lca(root.right, n1, n2)

    if l and r:
        return root
    if l:
        return l
    else:
        return r


def solve(root, a):
    if not root:
        return 0

    if root.data == a:
        return 1

    l = solve(root.left, a)
    r = solve(root.right, a)

    if not l and not r:
        return 0
    else:
        return l+r+1


def findDist(root, a, b):
    Lca = lca(root, a, b)
    x = solve(Lca, a)
    y = solve(Lca, b)
    return x+y-2
