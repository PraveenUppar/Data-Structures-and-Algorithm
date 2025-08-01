class Solution:
    def validPalindrome(self, s: str) -> bool:

        # left pointer - first index
        left = 0 
        # right pointer - last index
        right = len(s) - 1

        # loop till left is smaller than right
        while left < right:
            # if start and last element are not same
            if s[left] != s[right]:
                # two options either delete left element or right element
                # we need check for both
                skipL = s[left + 1 : right + 1]
                skipR = s[left : right]
                # if any of the condiiton is true then return TRUE or FALSE
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            left += 1
            right -= 1
        # if left and right element are equal for s then it is in palindrome form 
        return True

        # Brute Force - TLE

        # Checks if the input string is equal to reversed string if yes returns TRUE or starts loop
        # if s == s[::-1]:
        #     return True
        # for i in range(len(s)):
        #     # Refer Eg
        #     new_s = s[:i] + s[i + 1:]
        #     # Compare the new string with the resevsers new string if yes returns TRUE else return FALSE 
        #     if new_s == new_s[::-1]:
        #         return True
        # return False

        # Eg: s = "abca"
        # n = len(s) = 4 
        # new_s = s[:i] + s[i+1:]
        # at i = 0 = s[:i] = s[:0] = [""] + s[i+1:] = s[1:] = ["bca"] == ["bca"] - False
        # at i = 1 = s[:i] = s[:1] = ["a"] + s[i+1:] = s[2:] = ["ca"] == ["aca"] - True - Return
        # at i = 2 = s[:i] = s[:2] = ["ab"] + s[i+1:] = s[3:] = ["a"] == ["aba"] - True
        # at i = 3 = s[:i] = s[:3] = ["abc"] + s[i+1:] = s[4:] = [""] == ["abc"] - False