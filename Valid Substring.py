S = "(()))()(())("

stack = [-1]
maximum = 0
for i in range(len(S)):
    if S[i] == "(":
        stack.append(i)
    else:
        stack.pop()
        if stack == []:
            stack.append(i)
        maximum = max(maximum, i-stack[-1])
print(maximum)
# print(count1)

# print(len(S) - count - count1)
