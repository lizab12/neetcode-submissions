import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        h = {}

        for task in tasks:
            h[task] = h.get(task, 0) + 1

        heap = []

        for task, freq in h.items():
            heapq.heappush(heap, (-freq, task))

        c = 0

        while heap:

            temp = []
            check = 0

            for _ in range(n + 1):

                if not heap:
                    break

                freq, task = heapq.heappop(heap)

                c += 1
                check += 1

                freq += 1

                if freq < 0:
                    temp.append((freq, task))

            # Only tasks used in this cycle return now
            for item in temp:
                heapq.heappush(heap, item)

            # Need idle slots only if unfinished tasks remain
            if heap:
                c += (n + 1) - check

        return c