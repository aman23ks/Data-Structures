points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]


def get_distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


res = 0
for i in points:
    dic = {}
    for j in points:
        if i == j:
            continue
        d = get_distance(i, j)
        # print(f"{points[i]}:{points[j]}, dist: {d}")
        if d not in dic:
            dic[d] = 1
        else:
            dic[d] += 1
    for key, values in dic.items():
        # print(f"{key}:{values}")
        if values > 1:
            res += values*(values-1)
        # print(res)
print(res)


# def dist(p1, p2):
#     return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2


# res = 0
# for p1 in points:
#     # fix p1 as i
#     lookup = {}
#     for p2 in points:
#         if p1 == p2:
#             continue
#         d = dist(p1, p2)
#         if d in lookup:
#             lookup[d] += 1
#         else:
#             lookup[d] = 1

#     #  Find j and k as two element permutation: A_n^2 = n*(n-1)
#     for v in lookup.values():
#         if v > 1:
#             res += v*(v-1)
# print(res)
