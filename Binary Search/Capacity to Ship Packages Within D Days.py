# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. 
# Each day, we load the ship with packages on the conveyor belt (in the order given by weights). It is not allowed to load weight more than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.


def ship(weights, days):

    left = max(weights)
    right = sum(weights)
    weight = 0

    while left <= right:
        limit = (right + left) // 2
        curr_weight = 0
        curr_days = 1

        for i in weight:
            if curr_weight + i > limit:
                curr_days += 1
                curr_weight = i 
            else:
                curr_weight += i 

        if curr_days < days:
            weight = limit 
            right = limit - 1
        else:
            left = limit + 1
    return limit