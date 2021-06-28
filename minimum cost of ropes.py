# import Queue.PriorityQueue
import heapq


n = 4
arr = [4, 3, 2, 6]
sum = 0
heapq.heapify(arr)

res = 0

while(len(arr) > 1):

    first = heapq.heappop(arr)
    second = heapq.heappop(arr)

    res += first + second
    heapq.heappush(arr, first + second)

print(res)
