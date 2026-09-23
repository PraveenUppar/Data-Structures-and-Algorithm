def largest(arr):
    unique_nums = list(set(arr))
    
    if len(unique_nums) < 2:
        return None
    
    unique_nums.sort()           
    return unique_nums[-2]       

