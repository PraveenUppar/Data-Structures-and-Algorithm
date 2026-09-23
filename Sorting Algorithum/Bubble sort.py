arr = [4,6,8,3,1,7,5,9,2]


def bubbleSort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(bubbleSort(arr))