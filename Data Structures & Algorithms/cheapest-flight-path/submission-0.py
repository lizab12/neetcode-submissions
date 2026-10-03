class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        h = {i: [] for i in range(n)}

        for source, target, cost in flights:
            h[source].append((target, cost))

        bell = [float("inf")] * n
        bell[src] = 0

        for _ in range(k + 1):
            m = bell.copy()

            for i in range(n):

                if bell[i] != float("inf"):

                    for target, cost in h[i]:

                        m[target] = min(
                            m[target],
                            bell[i] + cost
                        )

            bell = m

        if bell[dst] == float("inf"):
            return -1

        return bell[dst]