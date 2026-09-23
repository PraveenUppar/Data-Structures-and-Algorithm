# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. 
# That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

def permutation(s1, s2):

    if len(s1) > len(s2):
        return False

    s1 = "".join(sorted(s1))

    for i in range(len(s2) - len(s1) + 1):
        substring = s2[i: i + len(s1)]
        sorted_str = "".join(sorted(substring))
        if sorted_str == s1:
            return True
    return False