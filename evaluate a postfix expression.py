stack = []

S = "123+*8-"

for i in S:
    if i.isdigit():
        stack.append(i)

    else:
        val1 = stack.pop()
        val2 = stack.pop()
        stack.append(str(eval(val2 + i + val1)))

print(stack.pop())
