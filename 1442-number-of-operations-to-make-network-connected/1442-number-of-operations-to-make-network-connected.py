class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        graph=defaultdict(list)
        

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            stack=[node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    stack.extend(graph[curr])

        components = -1
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components