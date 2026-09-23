# You are given two strings, word1 and word2. Construct a new string by merging them in alternating order, starting with word1
# take one character from word1, then one from word2, and repeat this process.

# If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result.

# Return the final merged string.

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