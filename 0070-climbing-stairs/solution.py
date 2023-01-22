class Solution:
    def __init__(self):
        self.cache = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        """
        O(n) time with caching, in this DP we start from the bottom aka the end result, and we have either go step down 1 or down 2 until we hit the result
        """
        if n not in self.cache:
            self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.cache[n]
    
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one += two
            two = temp
        return one

            
        
        
