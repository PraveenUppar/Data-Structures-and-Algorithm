class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        pair_arr = list(zip(position, speed))
        pair_arr.sort(reverse = True)

        for i in range(len(pair_arr)):
            distance = target - pair_arr[i][0]
            speed = pair_arr[i][1]
            time = distance/speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)