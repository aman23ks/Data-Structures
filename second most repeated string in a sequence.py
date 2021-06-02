# arr = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
arr = ["geek", "for", "geek", "for", "geek", "aaa"]
values = []
hashmap = {}
for i in arr:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1


for key, items in hashmap.items():
    values.append([items, key])

values.sort()
# print(values)
print(values[1][1])
