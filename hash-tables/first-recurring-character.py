# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# It should return 1

# Given an array = [2,3,4,5]
# It ahould return None.

# Brute force approach
index = []  # Initalize an empty index array


def recurr(input):
    for i in range(len(input)):  # Looping through the array if taking element as i
        for j in range(i+1, len(input)):  # Taking every succedding element as j
            # Comparing the 2 elements , if two similar elements are present (we push the index(j) in the index array)
            if input[i] == input[j]:
                if j in index:  # If j is already present go to the next element
                    break
                else:
                    # If j is not present add it to the index array.
                    index.append(j)
                    # sort the array so that the index with the smallest value occurs first.
                    index.sort()

    if not index:  # if the list index is empty return None
        return None
    else:
        # If index is not empty initialize c the first element of the index array as we will get the smallest index value after sorting(which represents the smallest index number after sorting(basically the very first repeated character))
        c = index[0]
        # take the index value and input it into c you'll get the occurence of the very first repeated character in array.
        return input[c]

# The time complexity is O(n^2) and the space complexity is O(1).


# Hash Table Approach

def recurr2(input):
    dictionary = dict()  # Initalize a empty dictionary
    for item in input:  # Looping one element at a time in the array
        if item in dictionary:  # Checking if item is already present in the dictionary
            print(dictionary)
            # If the item is present in the dictionary return the item.
            return item
        else:
            # If the item is not present in the dictionary assign the item as a key and a value true to it
            dictionary[item] = True
    return None  # If there is no recurring character return None.
# The time complexity of the process is O(n) . The space complexity is also O(n)


array = [3, 5, 2, 6, 9, 7, 4, 2, 8]
print(recurr(array))
