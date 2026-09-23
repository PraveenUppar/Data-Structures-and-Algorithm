# You are given a string s which contains only three types of characters: '(', ')' and '*'.

# Return true if s is valid, otherwise return false.

# A string is valid if it follows all of the following rules:

# Every left parenthesis '(' must have a corresponding right parenthesis ')'.
# Every right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".

def valid(s):

    stack1 = []
    stack2 = []


    for i, char in enumerate(s):

        if char == "(":
            stack1.append(i)

        elif char == ")":
            if stack1:
                stack1.pop()
            elif stack2:
                stack2.pop()
            else:
                return False
        else:
            stack2.append(i)

    while stack1 and stack2:
        if stack1[-1] > stack2[-1]:
            return False

        stack1.pop()
        stack2.pop()

    return len(stack1) == 0