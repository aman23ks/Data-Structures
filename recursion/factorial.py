# Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop


def findFactorialRecursive(number):
    if number <= 1:
        return 1
    else:
        return number * findFactorialRecursive(number-1)


print(findFactorialRecursive(7))


def findFactorialIterative(number):
    value = 1
    for i in range(number, 0, -1):
        value *= i
    return print(value)


findFactorialIterative(100)
