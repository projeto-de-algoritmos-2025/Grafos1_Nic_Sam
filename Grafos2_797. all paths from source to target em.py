class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = collections.defaultdict(list)

        for i, edges in enumerate(graph):
            self.graph[i] = edges

        res = []

        def dfs(cur_path, cur_node):
            if cur_node == len(self.graph) - 1:
                res.append(list(cur_path))
                return

            for connection in self.graph[cur_node]:
                cur_path.append(connection)
                dfs(cur_path, connection)
                cur_path.pop()

        dfs([0], 0)
        return res
