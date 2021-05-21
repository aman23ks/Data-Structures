nums = [1, 2, 3]

output = [[]]

for i in nums:
    output += [lst + [i] for lst in output]
print(output)