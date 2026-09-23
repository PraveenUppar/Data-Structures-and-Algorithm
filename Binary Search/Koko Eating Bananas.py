# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. 
# You are also given an integer h, which represents the number of hours you have to eat all the bananas.

# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

# Return the minimum integer k such that you can eat all the bananas within h hours.

import math

def koko(piles, h):
    left = 1
    right = max(piles)
    speed = right 

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for pile in piles:
            total += math.ceil(pile/mid)
        if total <= h:
            speed = mid 
            right = mid - 1
        else:
            left = mid + 1
    return speed