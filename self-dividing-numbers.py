left = 1
right = 22

# for i in range(left, right+1):
#     if i >= 10:
#         i = str(i)
#         for j in i:
#             i = int(i)
#             try:
#                 if i % int(j) == 0:

#             except ZeroDivisionError:
#                 continue
a = []


def check_num(x):
    for i in str(x):
        if i == "0" or x % int(i) != 0:
            return False
    return True


for i in range(left, right+1):
    if check_num(i):
        a.append(i)

print(a)
