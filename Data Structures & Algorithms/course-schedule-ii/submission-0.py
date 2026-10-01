class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        h = {}
        for i in prerequisites:
            if i[0] not in h:
                h[i[0]] = [i[1]]
            else:
                h[i[0]].append(i[1])
        
        m = []
        visiting, visited = set(), set()
        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)

            for j in h.get(i, []):
                if not dfs(j):
                    return False
            visiting.remove(i)
            visited.add(i)
            m.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return m