# class Item:
# def __init__(self,val,w):
# self.value = value
# self.weight = w


def fractionalknapsack(W, Items, n):
    arr = []
    total = 0
    s = 0
    for i in range(n):
        x = Items[i].value / Items[i].weight
        arr.append([x, i])

    arr.sort(reverse=True)

    for i in range(n):
        if s+Items[arr[i][1]].weight < W:
            total += Items[arr[i][1]].value
            s += Items[arr[i][1]].weight
        else:
            total += (W-s)*arr[i][0]
            break

    return total
