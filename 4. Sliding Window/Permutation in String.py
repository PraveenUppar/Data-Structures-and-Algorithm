class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # s1 = "ab" and s2 = "eiaboo"
        # Using counter as sliding window

        if len(s1) > len(s2):
            return False

        s1_counter = {} # Store the frequency of the s1 string 
        s2_counter = {} # Store the srequency of the s2 string 

        for i in range(len(s1)): # len(s1) is the number of elements we are looking in s2
            s1_counter[s1[i]] = 1 + s1_counter.get(s1[i],0) # addd the s1 elements in the s1 counter
            s2_counter[s2[i]] = 1 + s2_counter.get(s2[i],0) # add the s2 elements in the s2 counter till len(s1)

        # s1_counter = [a:1,b:1]
        # s2_counter = [e:1,i:1]
        # Compare both the string if they are same then we found permutaion
        if s1_counter == s2_counter:
            return True
        
        # s1 = "ab" len = 2
        # s2 = "eiaboo" len = 5
        # left = 0 and right = 2 to 5
        # s2 = "eiaboo" as [e:1,i:1] are in counter i.e(0,1) start right from 2 to 5
        left = 0
        for right in range(len(s1),len(s2)):
            # the window gets updated new element is added to counter and old element(left) is removed
            s2_counter[s2[right]] = 1 + s2_counter.get(s2[right],0)
            s2_counter[s2[left]] -=1  # the reason we remove bcz we have already checed s1_counter != s2_counter

            # need to remove that have frequency of 0
            # s2_counter = [e:0,i:1,a:1] as it will interput with the length and comparsion of the counters
            if s2_counter[s2[left]] == 0:
                del s2_counter[s2[left]]

            left += 1

            if s1_counter == s2_counter:
                return True
        return False

        # Hash map - TLE O(n*m)
        # counter1 = {}
        # for c in s1:
        #     # Add all the elements to teh counter
        #     # a:1 and b:1
        #     counter1[c] = 1 + counter1.get(c,0)
        # need = len(counter1) # need = 2 (it helps to comapre how many elemetns need to be there in s2)

        # for i in range(len(s2)):
        #     counter2 = {}
        #     current = 0 # keep a count of how many elements we have encountered that are presetn in s1
        #     for j in range(i,len(s2)):
        #         # add the element to counter 2
        #         counter2[s2[j]] = 1 + counter2.get(s2[j],0)
        #         # if the element is not presetn in both the counter then no sense to continue so break(i++)
        #         if counter1.get(s2[j], 0) < counter2[s2[j]]:
        #             break
        #         # if the element is presetnt in both counter 1 and 2 then we have found 1 element so current +=1 
        #         if counter1.get(s2[j], 0) == counter2[s2[j]]:
        #             current += 1
        #         if current == need: # if we have fouund all the elemtns from s1 in s2
        #             return True
        # return False

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
