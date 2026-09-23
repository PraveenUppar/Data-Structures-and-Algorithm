arr = [4,6,8,3,1,7,5,9,2]


def selectionSort(arr):

    for i in range(len(arr)):
        smallest = i
        for j in range(i + 1, len(arr)):
            if  arr[j] < arr[smallest] :
                smallest = j 
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr

print(selectionSort(arr))