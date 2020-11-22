# Implement a function that reverses a string using iteration... and then recursion!
# value: 'yoyo mastery'
# should return: 'yretsam oyoy'

def reverseStringIteration(value):
    new_Value = []
    value = list(value)
    for i in range(len(value)-1, -1, -1):
        new_Value.append(value[i])
    return "".join(new_Value)


print(reverseStringIteration('yoyo mastery'))


def reverseStringRecurssion(value):
    # print(value)
    if len(value) == 0:
        return value
    else:
        # end = "" will print all the values in the same line.
        print(value[len(value)-1], end="")
        return reverseStringRecurssion(value[0:len(value)-1])


print(reverseStringRecurssion('yoyo mastery'))
