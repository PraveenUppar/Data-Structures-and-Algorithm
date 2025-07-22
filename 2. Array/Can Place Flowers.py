from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    count = 0
    length = len(flowerbed)
    i = 0
    while i < length:
        if flowerbed[i] == 0:
            # Check left neighbor (if exists)
            left_empty = (i == 0) or (flowerbed[i-1] == 0)
            # Check right neighbor (if exists)
            right_empty = (i == length - 1) or (flowerbed[i+1] == 0)
            
            if left_empty and right_empty:
                flowerbed[i] = 1 # Place a flower
                count += 1
                i += 1 # Skip next plot as it's now a neighbor
        
        if count >= n:
            return True
        i += 1
            
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
