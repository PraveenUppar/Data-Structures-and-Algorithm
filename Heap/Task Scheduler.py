
# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

# Return the minimum number of CPU cycles required to complete all tasks.

from collections import Counter

def task(tasks, n):

    count = Counter(tasks)
    max_freq = max(count.values())

    ideal = 0

    for freq in count.values():
        if freq == max_freq:
            ideal += 1

    time = (max_freq - 1) + (n  + 1) + ideal
    return max(len(tasks), time)