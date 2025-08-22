def insertion_sort(arr):

    n = len(arr)

    for i in range(1, n):
        key = arr[i]  # Element to be inserted
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

my_list = [12, 11, 13, 5, 6]
sorted_list = insertion_sort(my_list)
print(f"Sorted list: {sorted_list}")