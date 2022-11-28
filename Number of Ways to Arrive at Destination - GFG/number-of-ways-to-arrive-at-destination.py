#User function Template for python3

#User function Template for python3
import heapq as hq
from typing import List
from collections import defaultdict
import sys
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Your code here

        import heapq as hq


class Solution:
    def countPaths(self, n, roads):

        dest = n - 1

        adj_list = {}

        for i in range(n):
            adj_list[i] = []

        for i in roads:
            adj_list[i[1]].append([i[2], i[0]])
            adj_list[i[0]].append([i[2], i[1]])

        # print(adj_list)

        distance = [float("inf")] * n

        distance[0] = 0

        heap = [(0, 0)]

        ways = [0] * n

        ways[0] = 1

        while heap:

            curr = heap.pop(0)

            dis = curr[0]
            node = curr[1]

            for i in adj_list[node]:

                edW = i[0]
                adjNode = i[1]

                if dis + edW == distance[adjNode]:
                    ways[adjNode] = (ways[adjNode] + ways[node]) % (pow(10, 9)+7)

                elif dis + edW < distance[adjNode]:
                    distance[adjNode] = dis + edW
                    heap.append((dis + edW, adjNode))
                    ways[adjNode] = ways[node]
                    hq.heapify(heap)

        return ways[dest] % (pow(10, 9)+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        adj=[]
        
        for i in range(m):
            tmp =[]
            x,y,z=map(int,input().split())
            tmp.append(x)
            tmp.append(y)
            tmp.append(z)
            adj.append(tmp)
            
        
        
        
       
        obj = Solution()
        res = obj.countPaths(n, adj)
        
        print(res)
        

# } Driver Code Ends