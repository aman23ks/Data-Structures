# What is good code?
# - Readable
# - Scalable(Big-o is what allows us to measure this idea of scale)

# BIG-O asymptotic analysis
# nemo = ["nemo"]


# def myfunc(l):
#     for i in l:
#         if i == "nemo":
#             print('Found nemo')


# myfunc(nemo) #The finding nemo operation has a big O notation of O(n) --> Linear Time

# Now suppose you run the above code a 100 times a 1000 times it'll take more time than its taking now to run the code
# But thats also not ncessarily true because that also many factors which computer you are using speed of computer etc.
# So we use Big-O to measure the speed of the code.
# O(n!) = Horrible
# O(2 ^ n) = Horrible
# O(n ^ 2) = Horrible
# O(nlogn) = Bad
# O(n) = Fair
# O(log n) = Good
# O(1) = Excellent

# When we talk about BIG-O or scabable we mean as we grow bigger and bigger in input how much does the algorithm slow down. the lesser it slows down the better it is

# boxes = ["apple", "banana"]


# def myfunc(boxes):
#     print(boxes[0])


# myfunc(boxes)
# O(1) - Constant time
# Even if we have 1000 elements we are just grabing the first elemenet in the box

# boxes = ["apple", "banana","orange","lemon"]

# def myfunc(boxes):
#     print(boxes[0]) #O(1)
#     print(boxes[1]) #O(1)

# myfunc(boxes)
# Here boxes are printed in 2 times everytime .
# The combined time complexity is O(2).
# here even if we print the first 3 elements everytime. the time compleity will be O(3).
# But in BIG-O we dont look at the nitty gritty , all of them will have a time complexity of O(1).

# What is the Big O of the below function? (Hint, you may want to go line by line)
# Javascript code
# function funChallenge(input) {
#     let a = 10 #O(1) No matter how big the input is it runs only once
#     a = 50 + 3 #O(1)

#     for (let i=0  #O(n)
#          i < input.length
#          i++) {
#         anotherFunction() #O(n)
#         let stranger = true #O(n)
#         a++ #O(n)
#     }
#     return a #O(1)
# 3 + n + n+ n = BIG O(3+4n)
# O(3+4n) just gets simplified to O(n).
# }


# What is the Big O of the below function? (Hint, you may want to go line by line)
# function anotherFunChallenge(input) {
#     let a = 5 #O(1)
#     let b = 10 #O(1)
#     let c = 50 #O(1)
#     for (let i=0
#          i < input
#          i++) {
#         let x = i + 1 #O(n)
#         let y = i + 2 #O(n)
#         let z = i + 3 #O(n)
#     }
#     for (let j=0
#          j < input
#          j++) {
#         let p = j * 2 #O(n)
#         let q = j * 2 #O(n)
#     }
#     let whoAmI = "I don't know" #O(1)
# O(4+5n) => O(n)
# }
