from typing import List
class Solution:
    def dfs(self, node, visited, adj, parent):
        
        visited[node] = 1
        # print(visited)
        for j in adj[node]:
            if visited[j] == 0 and parent != j:
                if self.dfs(j, visited, adj, node):
                    return 1
            elif visited[j] == 1 and parent == j:
                continue
            elif visited[j] == 1 and parent != j:
                return 1
        
        return 0
            
            
            
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        visited = [0 for i in range(V)]
        
        for i in range(V):
            if visited[i] == 0:
                if self.dfs(i, visited, adj, i) == 1:
                    return 1
                else:
                    continue
        
        return 0

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends