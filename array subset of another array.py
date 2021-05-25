a1 = [11, 1, 13, 21, 3, 7]
a2 = [11, 3, 7, 1]


def isSubset(a1, a2):
    hashmap = dict()
    for i in a1:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    count = 0

    print(hashmap)

    for i in a2:
        if i in hashmap.keys():
            count += 1

    if count == len(a2):
        return True

    return False


print(isSubset(a1, a2))
