import heapq as hq

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        
        adj_list = {}

        for i in range(V):
            adj_list[i] = adj[i]

        heap = [[0,S]]
        
        distance = [float("inf")] * len(adj)
        
        distance[S] = 0

        visited = [0] * len(adj)
        


        while heap != []:
            
            curr = heap.pop(0)
            
            dis = curr[0]
            node = curr[1]
            
            for i in adj_list[node]:
                if dis + i[1] < distance[i[0]]:
                    distance[i[0]] = dis + i[1]
                    heap.append([distance[i[0]],i[0]])
                    hq.heapify(heap)
        return distance
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends