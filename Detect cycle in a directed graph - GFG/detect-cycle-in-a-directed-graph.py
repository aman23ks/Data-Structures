#User function Template for python3


class Solution:
    

    # def dfs(self,node, visited, visdfs, adj):

    #     visited[node] = True
        
    #     visdfs[node] = True
        
    #     for i in adj[node]:
    #         if visited[i] == True and visdfs[i] == True:
    #             return True
    #         elif visited[i] == False:
    #             if(self.dfs(i, visited, visdfs, adj)) == True:
    #                 return True
        
    #     visdfs[node] = False
        
    #     return False
    
    def dfs(self, node, visited, visdfs, adj):
        visited[node] = 1
        visdfs[node] = 1
        
        for j in adj[node]:
            if visited[j] == 1 and visdfs[j] == 1:
                return 1
            elif visited[j] == 0:
                if self.dfs(j, visited, visdfs, adj) == 1:
                    return 1
        
        visdfs[node] = 0
        
        return 0
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        # visited = [False for i in range(len(adj))]

        # visdfs = [False for i in range(len(adj))]
    
        # for i in range(len(adj)):
        #     if visited[i] == False:
        #         if self.dfs(i,visited,visdfs,adj) == True:
        #             return True
    
        # return False
        
                
                
        visited = [0 for i in range(V)]
        visdfs = [0 for i in range(V)]
        
        
        for i in range(V):
            if visited[i] == 0:
                if self.dfs(i,visited, visdfs, adj) == 1:
                    return 1
        
        return 0
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends