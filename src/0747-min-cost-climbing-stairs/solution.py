class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        bounds:
            n: [2, len(cost)]
        edge case:
            n < 2:
                return cost[i], since its n == 1 or n == 0, only one element
        
        recurrence relation:
            first: 
                - n - 1 < n
                - small before big
            second:
                - n - 2 < n
                - small before big
            cost[n] + min(first, second)
        """
        n = len(cost)
        first = cost[0] # i
        second = cost[1] # i + 1
        if n <= 2:
            return min(first, second)
        for i in range(2, n):
            curr = cost[i] + min(first, second)
            first = second
            second = curr
        
        return min(first, second)

