class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        def hasPath(src, target, visited):
            if src == target:
                return True

            visited.add(src)

            for nei in graph.get(src, []):
                if nei not in visited:
                    if hasPath(nei, target, visited):
                        return True

            return False

        for a, b in edges:
            # before adding edge, check if a and b
            # are already connected
            if a in graph and b in graph:
                if hasPath(a, b, set()):
                    return [a, b]

            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            graph[a].append(b)
            graph[b].append(a)