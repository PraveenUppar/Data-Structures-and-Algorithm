class Solution:
    def decodeString(self, s: str) -> str:
        char_stack = []
        int_stack = []
        curr_int = 0
        curr_char = ""

        for char in s:
            if char.isdigit():
                curr_int = curr_int * 10 + int(char)
            elif char == "[":
                int_stack.append(curr_int)
                char_stack.append(curr_char)
                curr_int = 0
                curr_char = ""
            elif char == "]":
                top_int = int_stack.pop()
                top_char = char_stack.pop()
                curr_char = top_char + curr_char * top_int
            else:
                curr_char += char
        return curr_char