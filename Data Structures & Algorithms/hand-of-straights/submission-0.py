import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}

        for x in hand:
            count[x] = count.get(x, 0) + 1

        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            start = heap[0]

            for x in range(start, start + groupSize):
                if x not in count:
                    return False

                count[x] -= 1

                if count[x] == 0:
                    del count[x]

                    # x must currently be the smallest element
                    if heap[0] != x:
                        return False

                    heapq.heappop(heap)

        return True