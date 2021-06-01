arr = [1, 4, 45, 6, 0, 19]
x = 51

l = 0
r = 0
sum = 0
mi = float("inf")

while l <= r and r < len(arr):
    while sum <= x and r < len(arr):
        sum += arr[r]
        r += 1

    while sum > x and l < r:
        mi = min(mi, r-l)
        sum -= arr[l]
        l += 1

print(mi)
