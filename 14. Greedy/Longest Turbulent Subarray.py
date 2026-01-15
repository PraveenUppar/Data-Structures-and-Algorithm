class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        # Brute Force
        # res = 1

        # for i in range(len(arr) - 1):
        #     if arr[i] == arr[i + 1]:
        #         continue
        #     if arr[i] > arr[i + 1]:
        #         sign = 1
        #     else:
        #         sign = 0
        #     j = i + 1

        #     while j < len(arr) - 1:
        #         if arr[j] == arr[j + 1]:
        #             break
        #         if arr[j] > arr[j + 1]:
        #             curr_sign = 1
        #         else:
        #             curr_sign = 0
        #         if sign == curr_sign:
        #             break
        #         sign = curr_sign
        #         j += 1
        #     res = max(res, j - i + 1) 
        # return res

        # Sliding Window

        left = 0
        right = 1
        res = 1
        prev_sign = ""

        while right < len(arr):
            
            if arr[right - 1] > arr[right]:
                current_sign = ">"
            elif arr[right - 1] < arr[right]:
                current_sign = "<"
            else:
                current_sign = "="

            if current_sign == "=":
                left = right
                prev_sign = ""
            
            elif current_sign == prev_sign:
                left = right - 1
                prev_sign = current_sign
                res = max(res, right - left + 1)
                
            else:
                res = max(res, right - left + 1)
                prev_sign = current_sign
                
            right += 1

        return res



        