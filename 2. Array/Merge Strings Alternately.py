def merge_alternately(word1: str, word2: str) -> str:
        
        merge = []
        i = 0

        while i < len(word1) or i < len(word2):  #Condition for the loop for the iterations
            if i < len(word1):
                merge.append(word1[i])
            if i < len(word2):
                merge.append(word2[i])
            i += 1
        return "".join(merge)

        # Alternate Solution - Using Two pointer    

        # m = len(word1)
        # n = len(word2)
        # i = 0
        # j = 0
        # result = []

        # while i < m or j < n:
        #     if i < m:
        #         result += word1[i]
        #         i += 1
        #     if j < n:
        #         result += word2[j]
        #         j += 1

        # return "".join(result)

# Test Cases
print(f"'{'abc'}', '{'pqr'}' -> '{merge_alternately('abc', 'pqr')}'")
print(f"'{'ab'}', '{'pqrs'}' -> '{merge_alternately('ab', 'pqrs')}'")
print(f"'{'abcd'}', '{'pq'}' -> '{merge_alternately('abcd', 'pq')}'")
print(f"'{''}', '{'abc'}' -> '{merge_alternately('', 'abc')}'")
print(f"'{'xyz'}', '{''}' -> '{merge_alternately('xyz', '')}'")
print(f"'{''}', '{''}' -> '{merge_alternately('', '')}'")
