class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        five = 0
        tens = 0

        for cash in bills:
            if cash == 5:
                five += 1
            elif cash == 10:
                five -= 1
                tens += 1
            elif tens > 0:
                five -= 1
                tens -= 1
            else:
                five -= 3
            if five < 0:
                return False
        return True
        