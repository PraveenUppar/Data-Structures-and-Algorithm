class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)
        min_capacity = right

        def ship_capacity(capacity):

            day = 1
            curr_capacity = capacity

            for weight in weights:
                if curr_capacity - weight < 0:
                    day += 1
                    if day > days:
                        return False
                    curr_capacity = capacity
                curr_capacity -= weight
            return True

        while left <= right:
            capacity = (left + right) // 2
            if ship_capacity(capacity):
                min_capacity = min(min_capacity,capacity)
                right = capacity - 1
            else:
                left = capacity + 1
        return min_capacity

