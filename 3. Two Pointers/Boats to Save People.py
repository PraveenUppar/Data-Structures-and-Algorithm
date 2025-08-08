class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # The reason to sort in ascending order to match the light person at first with the heavy person at the last
        people.sort() 
        boat_count = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            # Calculate the space left after onboarding heavy person 
            # if the space is equal or more than then the light person we can add him
            space_left = limit - people[right]
            # Add a person to the boat so count += 1 and person is removed from people array
            right -= 1
            boat_count += 1
            # Check if a light person can fit
            if left <= right and space_left >= people[left]:
                left += 1
        return boat_count
