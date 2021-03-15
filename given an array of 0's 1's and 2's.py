array = [0, 2, 1, 2, 0]

l = 0
m = 0
h = len(array)-1
while m <= h:
    if array[m] == 0:
        array[l], array[m] = array[m], array[l]
        l += 1
        m += 1
    elif array[m] == 1:
        m += 1
    else:
        array[h], array[m] = array[m], array[h]
        h -= 1
print(array)
