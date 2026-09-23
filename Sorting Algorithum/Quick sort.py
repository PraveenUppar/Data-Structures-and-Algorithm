arr = [4,6,8,3,1,7,5,9,2]


def quickSort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []
    mid = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            mid.append(num)

    return quickSort(left) + mid + quickSort(right)

print(quickSort(arr))