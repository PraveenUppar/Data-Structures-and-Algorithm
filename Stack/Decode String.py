# You are given an encoded string s, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. There will not be input like 3a, 2[4], a[a] or a[2].

# The test cases are generated so that the length of the output will never exceed 100,000.

def decodeString(s):
    string_stack = []
    count_stack = []
    cur = ""
    k = 0

    for c in s:
        if c.isdigit():
            k = k * 10 + int(c)
        elif c == "[":
            string_stack.append(cur)
            count_stack.append(k)
            cur = ""
            k = 0
        elif c == "]":
            temp = cur
            cur = string_stack.pop()
            count = count_stack.pop()
            cur += temp * count
        else:
            cur += c

    return cur