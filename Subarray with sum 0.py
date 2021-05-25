arr = [4, 2, -3, 1, 6]


def subArrayExists(arr):
    if 0 in arr:
        return True

    for i in arr:
        if i > 0:
            if -i in arr:
                return True
        if i < 0:
            if i in arr:
                return True
    return False


print(subArrayExists(arr))
