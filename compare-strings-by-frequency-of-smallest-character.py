queries = ["bbb", "cc"]
words = ["a", "aa", "aaa", "aaaa"]


# def MaximumFrequency(strings):
#     strings = sorted(strings)
#     return strings.count(strings[0])


# val = []
# for i in queries:
#     count_q = 0
#     for j in words:
#         if MaximumFrequency(i) >= MaximumFrequency(j):
#             continue
#         else:
#             count_q += 1
#     val.append(count_q)

# print(val)

tmpQueries, tmpWords = [], []
for i in words:
    tmpWords.append(i.count(min(i)))
for i in queries:
    tmpQueries.append(i.count(min(i)))
res = []
for i in tmpQueries:
    count = 0
    for j in tmpWords:
        if i < j:
            count += 1
    res.append(count)
print(res)
