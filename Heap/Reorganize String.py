# You are given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# You can return any possible rearrangement of s or return "" if not posssible.

from collections import Counter
import heapq

def rearrange(s):
    counts = Counter(s)
    max_heap = []


    for char, count in counts.items():
        max_heap.append([-count, char])

    heapq.heapify(max_heap)

    prev = None
    res = ""

    while max_heap or prev:
        if prev and not max_heap:
            return ""

        count, char = heapq.heappop(max_heap)
        res += char
        count += 1

        if prev:
            heapq.heappush(max_heap, prev)
            prev = None 

        if count != 0:
            prev = [count, char]

    return res