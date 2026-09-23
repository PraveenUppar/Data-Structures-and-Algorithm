# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# You are given three integers a, b, and c, return the longest possible happy string. 
# If there are multiple longest happy strings, return any of them. 
# If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

import heapq

def longest(a, b, c):

    max_heap = []

    if a > 0:
        heapq.heappush(max_heap, (-a, "a"))
    if b > 0:
        heapq.heappush(max_heap, (-b, "b"))
    if c > 0:
        heapq.heappush(max_heap, (-c, "c"))

    res = []

    while max_heap:

        count1, char1 = heapq.heappop(max_heap)

        if len(res) >= 2 and res[-1] == res[-2] == char1:

            if not max_heap:
                break

            count2, char2 = heapq.heappop(max_heap)
            res.append(char2)

            if count2 + 1 < 0:
                heapq.heappush(max_heap, (count2 + 1, char2))

            heapq.heappush(max_heap, (count1 + 1, char1))  
            
        else:
            res.append(char1)
            if count1 + 1 < 0:
                heapq.heappush(max_heap, (count1 + 1, char1))

    return "".join(res)