str = "abcdef"


def func(t, i, n, str):
    if i == n:
        print(t)
    else:
        func(t, i+1, n, str)
        t = t + str[i]
        func(t, i+1, n, str)


func("", 0, len(str), str)
