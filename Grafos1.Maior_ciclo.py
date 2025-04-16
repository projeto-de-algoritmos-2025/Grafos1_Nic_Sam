class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        def dfs(node, lenSoFar, callstack):
            if node == -1:
                return

            if node in self.visited:

                i = -1
                for j in range(len(callstack)):
                    if callstack[j] == node:  
                        i = j  
                        break
                if i == -1: 
                    return

                cycleLen = lenSoFar - i
                self.best = max(self.best, cycleLen)
                return

            self.visited.add(node)
            callstack.append(node)
            dfs(edges[node], lenSoFar + 1, callstack)

        n = len(edges)
        self.visited = set()
        self.best = -1

        for node in range(n):
            if node not in self.visited:
                dfs(node, 0, [])

        return self.best
