class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # eg: s1 = "ab" and s2 = "eiaboo"
        # eg: s1 = "ab" and s2 = "eiaoob"
        
        counter1 = {}
        for c in s1:
            # Add all the elements to teh counter
            # a:1 and b:1
            counter1[c] = 1 + counter1.get(c,0)
        need = len(counter1) # need = 2 (it helps to comapre how many elemetns need to be there in s2)

        for i in range(len(s2)):
            counter2 = {}
            current = 0 # keep a count of how many elements we have encountered that are presetn in s1
            for j in range(i,len(s2)):
                # add the element to counter 2
                counter2[s2[j]] = 1 + counter2.get(s2[j],0)
                # if the element is not presetn in both the counter then no sense to continue so break(i++)
                if counter1.get(s2[j], 0) < counter2[s2[j]]:
                    break
                # if the element is presetnt in both counter 1 and 2 then we have found 1 element so current +=1 
                if counter1.get(s2[j], 0) == counter2[s2[j]]:
                    current += 1
                if current == need: # if we have fouund all the elemtns from s1 in s2
                    return True
        return False

        # Brute Force - O(n**3logn)
        # s1 = sorted(s1)

        # for i in range(len(s2)):
        #     for j in range(i,len(s2)):
        #         # Finding every combination from s2 and comapring it with s1
        #         sub_string = s2[i:j+1]
        #         sub_string = sorted(sub_string)
        #         if sub_string == s1:
        #             return True
        # return False
