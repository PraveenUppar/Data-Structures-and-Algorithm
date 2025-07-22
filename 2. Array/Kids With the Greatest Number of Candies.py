from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    
    max_candies = max(candies)
    
    result = []

    for candy_count in candies:
        if candy_count + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result

# Test Cases
print(f"Candies: [2,3,5,1,3], Extra Candies: 3 -> {kidsWithCandies([2,3,5,1,3], 3)}")
print(f"Candies: [4,2,1,1,2], Extra Candies: 1 -> {kidsWithCandies([4,2,1,1,2], 1)}")
print(f"Candies: [12,1,12], Extra Candies: 10 -> {kidsWithCandies([12,1,12], 10)}")
print(f"Candies: [1,1,1,1,1], Extra Candies: 0 -> {kidsWithCandies([1,1,1,1,1], 0)}")
print(f"Candies: [10], Extra Candies: 5 -> {kidsWithCandies([10], 5)}")
