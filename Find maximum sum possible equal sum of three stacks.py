stack1 = [3, 2, 1, 1, 1]
stack2 = [4, 3, 2]
stack3 = [1, 1, 4, 1]


def max_stack(stack1, stack2, stack3):
    sum1 = sum(stack1)
    sum2 = sum(stack2)
    sum3 = sum(stack3)

    while sum1 != sum2 != sum3 or sum1 == sum2 == sum3 == 0:
        if sum1 > sum2 and sum3:
            stack1.pop(0)
            sum1 = sum(stack1)
        elif sum2 > sum1 and sum3:
            stack2.pop(0)
            sum2 = sum(stack2)
        elif sum3 > sum1 and sum2:
            stack3.pop(0)
            sum3 = sum(stack3)

    return sum1


print(max_stack(stack1, stack2, stack3))
