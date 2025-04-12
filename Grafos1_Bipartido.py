from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                q = deque([node]) 
                while q:
                    node = q.popleft()
                    for nei in graph[node]:
                        if nei in color:
                            if color[nei] == color[node]:  
                                return False        
                        else:
                            q.append(nei)
                            color[nei] = color[node] ^ 1 
        return True


graph1 = [[1,3],[0,2],[1,3],[0,2]]
graph2 = [[1,2,3],[0,2],[0,1,3],[0,2]]

sol = Solution()
print("Grafo 1 é bipartido?", sol.isBipartite(graph1))  
print("Grafo 2 é bipartido?", sol.isBipartite(graph2)) 
