arr = [3, 1, 7, 1]

arr.sort()

print(arr)
sum1 = sum(arr)
sum2 = 0
count = 0
for i in range(len(arr)-1, -1, -1):
    if sum2 > sum1:
        break
    else:
        sum1 -= arr[i]
        count += 1
        sum2 += arr[i]

print(count)
