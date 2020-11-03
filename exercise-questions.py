# Example Qestion 1
# My solution - correct answer but very high time complexity O(n^2)
def myfunc():
    list1 = ['a', 'b', 'c', 'd']
    list2 = ['x', 'g', 'j', 'f']
    x = False
    for i in list1:
        for j in list2:
            if(i == j):
                x = True
                return print(x)
    return print(x)


myfunc()


# Hash Maps solution - efficient code.
# Javascript code

# const array1 = ['a', 'b', 'c', 'x']
# const array2 = ['z', 'y', 'a']

# function containsCommonItem2(arr1, arr2) {
#     // loop through first array and create object where properties === items in the array
#     // can we assume always 2 params?

#     let map = {}
#     for (let i=0
#          i < arr1.length
#          i++) {
#         if(!map[arr1[i]]) {
#             const item = arr1[i]
#             map[item] = true
#         }
#     }
#     // loop through second array and check if item in second array exists on created object.
#     for (let j=0
#          j < arr2.length
#          j++) {
#         if (map[arr2[j]]) {
#             return true
#         }
#     }
#     return false
# }

# //O(a + b) Time Complexity
# //O(a) Space Complexity

# // containsCommonItem2(array1, array2)

# function containsCommonItem3(arr1, arr2) {
#     return arr1.some(item=> arr2.includes(item))
# }

# containsCommonItem(array1, array2)
# containsCommonItem2(array1, array2)
# containsCommonItem3(array1, array2)
