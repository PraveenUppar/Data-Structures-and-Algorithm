class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        max_freq_task = max(count)

        task_with_same_max_freq = 0
        for i in count:
            if i == max_freq_task:
                task_with_same_max_freq += 1
            else:
                0

        time = (max_freq_task - 1) * (n + 1) + task_with_same_max_freq
        return max(len(tasks), time)

# The built-in ord() function returns the Unicode code point of a single character. 
# For example, ord('A') is 65, ord('B') is 66, 

# ord(task) - ord('A')
# If task is 'A', ord('A') - ord('A') is 0.
# If task is 'B', ord('B') - ord('A') is 1.
# If task is 'C', ord('C') - ord('A') is 2, and so on.
        