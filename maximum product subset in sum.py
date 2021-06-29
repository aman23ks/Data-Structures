a = [-2, -4, 2, 3]

zero_count = 0
negative_count = 0
prod = 1
max_negative = float("-inf")

for i in range(len(a)):
    if a[i] == 0:
        zero_count += 1
        continue
    elif a[i] < 0:
        negative_count += 1
        max_negative = max(a[i], max_negative)
    prod *= a[i]

if zero_count == len(a):
    print(0)
elif negative_count == 1 and zero_count+negative_count == len(a):
    print(0)
else:
    if negative_count % 2 == 0:
        print(prod)
    else:
        prod = prod/max_negative
        print(prod)
