from collections import Counter

def counting_sort(arr):
    count = Counter(arr)
    output = []
    for c in sorted(count.keys()):
        output += [c] * count[c]
    return output

arr = "geeksforgeeks"
arr = list(arr)
arr = counting_sort(arr)
output = ''.join(arr)
print("Sorted character array is", output)