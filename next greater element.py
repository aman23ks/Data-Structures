arr = [1, 3, 2, 4]
n = len(arr)

stack = []
stack.append(0)
output = [None]*n


# def check(stack, arr):
#     if arr[i] > arr[stack[-1]]:
#         output[stack[-1]] = arr[i]
#         stack = stack[:-1]
#     return


for i in range(1, len(arr)):
    print(stack)

    if stack == []:
        stack.append(i)

    if arr[i] <= arr[stack[-1]]:
        stack.append(i)

    elif arr[i] > arr[stack[-1]]:
        output[stack[-1]] = arr[i]
        print(output)
        stack.pop()
        while stack:
            if arr[i] > arr[stack[-1]]:
                output[stack[-1]] = arr[i]
                stack.pop()
            else:
                break
        # check(stack, arr)
        stack.append(i)
        print(stack)


print(stack)
while stack:
    output[stack.pop()] = -1

print(output)
