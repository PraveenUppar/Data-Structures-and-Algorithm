class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # if the len of num and the value of k are same then the each element has freq of 1
        # Eg: nums = [1,1,1] and k = 3 ans = [1,1,1] which is wrong bcz it should return only [1]
        # Eg: nums = [1,2,3] and k = 3 ans = [1,2,3] which is correct here k is not the frequency
        if k == len(nums):
            return nums
                            
        # Counter function does same as hash map dont buils hashmap from scrach just use counter function
        freq = Counter(nums)
        sorted_items_freq = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))

        # To store and return the elements from the hash map with k most freq
        result_keys = []
        # Keep the count of k so that we dont exceed the k element count
        k_count = 0

        # In freq you have to return the keys which freq is largest to smallest upto to kth element
        for key, value in sorted_items_freq.items():
            if k_count < k:
                result_keys.append(key)
                k_count += 1
        return result_keys

        # OR 
        # return sorted_items_freq[:k]

# find out the K most frequent items and not "Which element is K times repeated"


# SOUTION 

# freq = Counter(nums)
# sorted_items_freq = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))
# retrun sorted_items_freq[:k]