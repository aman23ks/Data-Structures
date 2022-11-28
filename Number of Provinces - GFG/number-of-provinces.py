#User function Template for python3


class Solution:
    def dfs(self, node, adj, visited):
        
        visited[node] = 1
        
        for i in adj[node]:
            if visited[i] == 0:
                self.dfs(i, adj, visited)
    
    
    def numProvinces(self, adj, V):
        # code here 
        isConnected = adj    
    
        n = len(isConnected)
        visited = [0]*n
        count = 0
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else:
                    if isConnected[i][j] == 1:
                        adj[i].append(j)
        
        for i in adj:
            if visited[i] == 0:
                self.dfs(i,adj,visited)
                count += 1
                
        return count
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends