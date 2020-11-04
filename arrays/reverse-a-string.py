# Create a function that reverses a string
# Hi My name is Aman
# namA si eman yM iH

array = "Hi My name is Aman"


def reverse(arr):
    reversedArray = []  # Declaring a empty list
    for i in range(len(arr)-1, -1, -1):  # Looping from last element to 0 and decrementing by 1
        # adding the last element to the reversedArray list
        reversedArray.append(arr[i])
    # if only return reversedArray ['n', 'a', 'm', 'A', ' ', 's', 'i', ' ', 'e', 'm', 'a', 'n', ' ', 'y', 'M', ' ', 'i', 'H']
    # to remove the '' we do the join function
    return ''.join(reversedArray)
    # The time complexity is O(n)


print(reverse(array))


# or simply just do
# print(array[::-1]) # In this case the time complexity is O(1)
