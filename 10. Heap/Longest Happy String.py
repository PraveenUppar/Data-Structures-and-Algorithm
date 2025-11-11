class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, "a"))
        if b > 0:
            heapq.heappush(pq, (-b, "b"))
        if c > 0:
            heapq.heappush(pq, (-c, "c"))

        result = []
        while pq:
            count, char = heapq.heappop(pq)
            count = -count
            if (len(result) >=2 and result[-1] == char and result[-2] == char):
                if not pq:
                    break
                tempcount, tempchar = heapq.heappop(pq)
                result.append(tempchar)
                if (tempcount + 1) < 0:
                    heapq.heappush(pq, (tempcount + 1, tempchar))
                heapq.heappush(pq, (-count, char))
            else:
                count -= 1
                result.append(char)
                if count > 0:
                    heapq.heappush(pq, (-count, char))
        return "".join(result)



        