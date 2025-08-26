class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans


        # Brute Force O(n**2)
        # ans = []

        # for i in range(len(temperatures)):
        #     count = 1
        #     j = i + 1
        #     while j < len(temperatures):
        #         if temperatures[i] < temperatures[j]:
        #             break
        #         else:
        #             count += 1
        #             j += 1
        #     count = 0 if j == len(temperatures) else count
        #     ans.append(count)
        # return ans

        