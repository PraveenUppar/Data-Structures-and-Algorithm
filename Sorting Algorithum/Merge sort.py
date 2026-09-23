arr = [4,6,8,3,1,7,5,9,2]

def merge(left, right):
        i = 0
        j = 0
        merged_arr = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged_arr.append(left[i])
                i += 1
            else:
                merged_arr.append(right[j])
                j += 1
        while i < len(left):
            merged_arr.append(left[i])
            i += 1
        while j < len(right):
            merged_arr.append(right[j])
            j += 1
        return merged_arr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    sorted_left = mergeSort(left)
    sorted_right = mergeSort(right)
    return merge(sorted_left, sorted_right)

print(mergeSort(arr))