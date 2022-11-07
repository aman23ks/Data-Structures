#User function Template for python3
import heapq as hq 
class Solution:
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        visited = [0]*V

        heap = [[0, 0]]
        sum = 0

        while heap != []:
            node = hq.heappop(heap)
            wt = node[0]
            curr = node[1]

            if visited[curr] == 1:
                continue
            
            visited[curr] = 1
            sum += wt

            for i in adj[curr]:
                edW = i[1]
                ele = i[0]

                if visited[ele] == 0:
                    hq.heappush(heap, [edW, ele])
        
        return sum
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends