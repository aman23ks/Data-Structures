def PalinArray(arr):

    for i in arr:
        if str(i) == str(i)[::-1]:
            continue
        else:
            return 0

    return 1
