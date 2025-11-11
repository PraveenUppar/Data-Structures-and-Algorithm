class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = []
        for passenger, pickup, drop in trips:
            locations.append([pickup, passenger])
            locations.append([drop, -passenger])

        locations.sort()
        curr_passengers = 0

        for pickup, passenger in locations:
            curr_passengers += passenger
            if curr_passengers > capacity:
                return False
        return True
        
