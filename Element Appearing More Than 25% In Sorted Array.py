arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]

percent = len(arr)*0.25

ele = {}

for i in arr:
    if i not in ele:
        ele[i] = 1
    else:
        ele[i] += 1

for key, value in ele.items():
    if value > percent:
        print(key)
