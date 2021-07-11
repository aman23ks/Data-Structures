
# N = 4
# K = 2
# candies = [3, 2, 1, 4]

N = 5
K = 4
candies = [3, 2, 1, 4, 5]


candies.sort()

min = 0
max = 0

i = 0
j = N-1

while i <= j:
    min += candies[i]
    i += 1
    j -= K

candies.reverse()

i = 0
j = N-1

while i <= j:
    max += candies[i]
    i += 1
    j -= K

print(min, max)
