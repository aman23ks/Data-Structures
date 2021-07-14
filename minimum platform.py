def minimumPlatform(n, arr, dep):
    arr.sort()
    dep.sort()
    i = 1
    plt_no = 1
    j = 0
    while i < n:
        if arr[i] <= dep[j]:
            plt_no += 1
        else:
            j += 1

        i += 1

    return plt_no
