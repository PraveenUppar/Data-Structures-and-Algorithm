class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {")":"(", "]":"[", "}":"{"}
        stack = []

        for i in s:
            if i in hashmap:
                if stack and stack[-1] == hashmap[i]:
                    stack.pop()
            else:
                stack.append(i)
        return True if not stack else False

        # Not using hashmap - O(n)
        # stack = []
        # for i in s:
        #     if i == "(" or i == "{" or i == "[":
        #         stack.append(i)
        #     elif i == ")":
        #         if stack and stack[-1] == "(":
        #             stack.pop()
        #         else:
        #             return False
        #     elif i == "}":
        #         if stack and stack[-1] == "{":
        #             stack.pop()
        #         else:
        #             return False
        #     elif i == "]":
        #         if stack and stack[-1] == "[":
        #             stack.pop()
        #         else:
        #             return False
        # return True if not stack else False

        # Burte Force - O(n**2))
        # while "()" in s or "{}" in s or "[]" in s:
        #     s = s.replace("()", "")
        #     s = s.replace("[]", "")
        #     s = s.replace("{}", "")
        # return s == ""