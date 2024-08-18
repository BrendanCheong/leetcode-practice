class Solution:
    def canJump(self, nums: List[int]) -> bool:
        travel_power = 0
        for n in nums:
            if travel_power < 0:
                return False
            # Greedily take the highest num we can see if we need it
            elif n > travel_power:
                travel_power = n
            travel_power -= 1
        return True
