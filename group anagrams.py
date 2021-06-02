strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
hashmap = {}

for i in strs:
    ele = "".join(sorted(i))
    if ele not in hashmap:
        hashmap[ele] = [i]
    else:
        hashmap[ele].append(i)

values = []
for i in hashmap.values():
    values.append(i)
print(values)
