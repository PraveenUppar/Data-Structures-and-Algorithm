# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. 
# You need to use all the matchsticks to make one square. You should not break any stick, but you can link them up, 
# and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.


def makesquare(self, matchsticks):

    if len(matchsticks) <= 3:
        return False
    
    if sum(matchsticks) % 4 != 0:
        return False
    
    sides = [0] * 4
    target = sum(matchsticks) // 4
    matchsticks.sort(reverse=True)

    def backtracking(i):
        if i == len(matchsticks):
            return True
        
        for j in range(4):
            if sides[j] + matchsticks[i] <= target:
                sides[j] += matchsticks[i]
                if backtracking(i+1):
                    return True
                sides[j] -= matchsticks[i]
        return False

    return backtracking(0)
    