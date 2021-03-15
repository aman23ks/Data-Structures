num1 = [1, 2, 3, 4, 5]
num2 = [1, 2, 3]

union_values = []


def values(array):
    for i in array:
        if i in union_values:
            continue
        else:
            union_values.append(i)


values(num1)
values(num2)

print(union_values)
