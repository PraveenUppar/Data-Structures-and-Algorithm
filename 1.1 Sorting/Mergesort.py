def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: a list with 0 or 1 element is already sorted

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged_list = []
    i = 0  # Pointer for the left list
    j = 0  # Pointer for the right list

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    # Add any remaining elements from the left list
    while i < len(left):
        merged_list.append(left[i])
        i += 1

    # Add any remaining elements from the right list
    while j < len(right):
        merged_list.append(right[j])
        j += 1

    return merged_list

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(my_list)
print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")