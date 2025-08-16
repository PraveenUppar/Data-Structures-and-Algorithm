class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        need_counter = {}

        for i in t:
            need_counter[i] = 1 + need_counter.get(i ,0)
        
        want_counter = {}

        need_char = len(need_counter)
        want_char = 0

        window = [-1,-1]
        window_len = float("inf")

        left = 0

        for right in range(len(s)):

            want_counter[s[right]] = 1 + want_counter.get(s[right] , 0)

            if s[right] in need_counter and want_counter[s[right]] == need_counter[s[right]]:
                want_char += 1

            while need_char == want_char:
                if right - left + 1 < window_len:
                    window = [left,right]
                    window_len = right - left + 1
                
                want_counter[s[left]] -= 1

                if s[left] in need_counter and want_counter[s[left]] < need_counter[s[left]]:
                    want_char -= 1
                
                left += 1

        left,right = window
        return s[left:right + 1] if window_len != float("inf") else ""