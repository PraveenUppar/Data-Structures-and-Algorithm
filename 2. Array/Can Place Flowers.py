from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:

    count = 0
    
    for i in range(len(flowerbed)):
        # Check if the current plot is empty.
        if flowerbed[i] == 0:
            # Check if the left and right plots are empty.
            # Flowerbed: [0,0,1,0,0], n = 2 ouput- True(it is possible at 1st and last index)
            # Consider the edge cases also so theere will be 4 condition
            # condition 1 that is the i is at 0th index and condition 2 will be ith is at last index
            # condition 3 and 4 will be the preious and the next element must be zero
            empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
            # If both plots are empty, we can plant a flower here.
            if empty_left_plot and empty_right_lot:
                flowerbed[i] = 1
                count += 1
                    
    return count >= n

# Test Cases
print(f"Flowerbed: [1,0,0,0,1], n = 1 -> {canPlaceFlowers([1,0,0,0,1], 1)}")
print(f"Flowerbed: [1,0,0,0,1], n = 2 -> {canPlaceFlowers([1,0,0,0,1], 2)}")
print(f"Flowerbed: [0,0,1,0,0], n = 1 -> {canPlaceFlowers([0,0,1,0,0], 1)}")
print(f"Flowerbed: [0,0,1,0,0], n = 2 -> {canPlaceFlowers([0,0,1,0,0], 2)}")
print(f"Flowerbed: [1,0,1,0,1], n = 0 -> {canPlaceFlowers([1,0,1,0,1], 0)}")
print(f"Flowerbed: [0,0,0,0,0], n = 3 -> {canPlaceFlowers([0,0,0,0,0], 3)}")
print(f"Flowerbed: [0], n = 1 -> {canPlaceFlowers([0], 1)}")
print(f"Flowerbed: [1], n = 0 -> {canPlaceFlowers([1], 0)}")
print(f"Flowerbed: [0,0], n = 1 -> {canPlaceFlowers([0,0], 1)}")
print(f"Flowerbed: [1,0], n = 1 -> {canPlaceFlowers([1,0], 1)}")
print(f"Flowerbed: [0,1], n = 1 -> {canPlaceFlowers([0,1], 1)}")
