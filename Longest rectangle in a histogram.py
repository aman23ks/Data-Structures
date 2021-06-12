# heights = [2, 1, 5, 6, 2, 3]
heights = [2, 4]


def largestRectangleArea(heights):
    n = len(heights)
    left = []
    right = []
    stack = []

    for i in range(n):
        if stack == []:
            left.append(0)
            stack.append(i)
        else:
            while stack != [] and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack == []:
                left.append(0)
                stack.append(i)
            else:
                left.append(stack[-1] + 1)
                stack.append(i)

    stack = []

    for i in range(n-1, -1, -1):
        if stack == []:
            right.append(n-1)
            stack.append(i)
        else:
            while stack != [] and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack == []:
                right.append(n-1)
                stack.append(i)
            else:
                right.append(stack[-1] - 1)
                stack.append(i)

    right = right[::-1]
    maximum = 0
    for i in range(n):
        maximum = max(maximum, (right[i] - left[i] + 1)*heights[i])

    return maximum


print(largestRectangleArea(heights))
