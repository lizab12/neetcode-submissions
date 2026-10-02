class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        minDist = [float("inf")] * n
        minDist[0] = 0

        visited = set()
        total = 0

        for _ in range(n):
            cur = -1

            # pick unvisited node with smallest connection cost
            for i in range(n):
                if i not in visited:
                    if cur == -1 or minDist[i] < minDist[cur]:
                        cur = i

            visited.add(cur)
            total += minDist[cur]

            # update cheapest distance to remaining nodes
            for j in range(n):
                if j not in visited:
                    d = abs(points[cur][0] - points[j][0]) + \
                        abs(points[cur][1] - points[j][1])

                    minDist[j] = min(minDist[j], d)

        return total