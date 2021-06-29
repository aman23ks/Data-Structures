from sortedcontainers import SortedSet

A = "abba"
new_s = ""
s = SortedSet()
for i in range(len(A)):
    s.add(A[i])
# print(s)
for i in range(len(A)):
    try:
        ch1 = s[0]
        # print(ch1)
        s.remove(A[i])
        if len(s) == 0:
            break
        if ord(ch1) < ord(A[i]):
            ch2 = A[i]
            for j in range(len(A)):
                if A[j] == ch1:
                    new_s += ch2
                elif A[j] == ch2:
                    new_s += ch1
                else:
                    new_s += A[j]
            break
    except KeyError:
        continue

if new_s == "":
    print(A)
else:
    print(new_s)
