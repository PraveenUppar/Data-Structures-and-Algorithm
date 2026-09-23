# You are given an integer array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. 
# Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

def rescue(people, limit):
    people.sort()
    boats = 0
    left = 0
    right = len(people) - 1

    while left < right:

        boats += 1
        weight = people[left] + people[right]

        if weight <= limit:
            left += 1

        right -= 1

    return boats