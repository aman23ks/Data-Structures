<<<<<<< HEAD
# Sum of a pair of  numbers in an array is equal to the value given.
# We have to check if there are any two elements in the array that add up to the sum.

array = [2, 6, 3, 7, 8]
sum = 9

# For example 3+6 = 9 in the above case.

# The very first approach that comes to mind is the navie , or brute force approach so lets implement that:


def brute_force_pair_sum(array, sum):
    for i in range(len(array)):
        for j in range(j+1, len(array)):
            if array[i] + array[j] == sum:
                return "Yes"
    return "No"


# print the solution
print(brute_force_pair_sum(array, sum))
# As we can see the complexity of the function is O(n^2).Which will become very inefficient for large inputs.
# So we need to optimize the function.

# Binary search part will do after learning the concepts . For now just the brute force approach.
=======
# Sum of a pair of  numbers in an array is equal to the value given.
# We have to check if there are any two elements in the array that add up to the sum.

array = [2, 6, 3, 7, 8]
sum = 9

# For example 3+6 = 9 in the above case.

# The very first approach that comes to mind is the navie , or brute force approach so lets implement that:


def brute_force_pair_sum(array, sum):
    for i in range(len(array)):
        for j in range(j+1, len(array)):
            if array[i] + array[j] == sum:
                return "Yes"
    return "No"


# print the solution
print(brute_force_pair_sum(array, sum))
# As we can see the complexity of the function is O(n^2).Which will become very inefficient for large inputs.
# So we need to optimize the function.

# Binary search part will do after learning the concepts . For now just the brute force approach.
>>>>>>> 131d0d1671889eaa6b3bed79e984371a88502a5f
