# Write a iterative code and recursive code for a fibonacci sequence.

def fibonacciRecurssive(number):  # O(2^n) - time complexity more worse than O(n^2)
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacciRecurssive(number-1) + fibonacciRecurssive(number-2)


print(fibonacciRecurssive(10))


def fibonacciIterative(number):  # O(n) - time complexity
    array = [0, 1]
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        for i in range(2, number+1, 1):
            i = array[i-1] + array[i-2]
            array.append(i)
        return array[len(array)-1]


print(fibonacciIterative(10))
