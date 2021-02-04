# even length
# split into equal length a(first half) and b(second half)

s = "AbCdEfGh"
a = []
b = []
for i in range(len(s)):
    if i < (len(s)/2):
        a.append(s[i])
    else:
        b.append(s[i])

a = "".join(a).upper()
b = "".join(b).upper()

a_count = 0
b_count = 0

for i in a:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        a_count += 1

for i in b:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        b_count += 1

if a_count == b_count:
    print(True)
else:
    print(False)
