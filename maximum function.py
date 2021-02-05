arr = [10, 2, 8, 7]
value = []

for i in range(len(arr)-2):
    for j in range(len(arr)-1):
        new_arr = []

        if i == j:
            continue
        else:
            new_arr.append(arr[i])
            new_arr.append(arr[j])
            if i == j+1:
                continue
            else:
                new_arr.append(arr[j+1])

            print(new_arr)
            sum_new_arr = abs(
                new_arr[0]-new_arr[1]) + abs(new_arr[1]-new_arr[2]) + abs(new_arr[2]-new_arr[0])
            if sum_new_arr not in value:
                value.append(sum_new_arr)


print(max(value))
