class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]   # [-2, -7, -4, -1, -8, -1]
        heapq.heapify(stones)           # [-8, -7, -4, -1, -2, -1]

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])