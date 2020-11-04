# Arrays
# Consider you have a array(or list in python)
array = ['a', 'b', 'c', 'd']

# Here on a 32bit system each value will take up 4bytes of memory, so together they will store 16 bytes of memory

# accesing elements
print(array[1])  # time complexity O(1)

# append function
# Since the append function just adds one element to the end of array its time complexity is O(1).
array.append('e')

# pop function
# Since the pop function just removes an element from the end of the array it has a time complexity of O(1).
array.pop()

# insert
# Since in this case when we insert an element we reassign all the elements a new value (a is assigned index 1 from 0, b is assigned 2 from 1 and so on...)
array.insert(0, 'x')
array.insert(2, 'alien')  # time complextiy O(n/2) -> O(n)
# And depending on the size of the array.

# deleting
# This element removes the 3 element from the array and shifts all the elements ahead one step backwards
array.pop(3)
# It has a time complexity of O(n).
# This method finds the method you want to remove and deletes it and shifts all the elements ahead of it one step backwards.
array.remove('d')
# It has a time complexity of O(n).
del array[1:3]

print(array)
