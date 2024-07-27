class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # exit when slow and fast intersect and collide with each other
        while True:
            slow = nums[slow]
            # fast pointer is twice as fast as the slow
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # 2. Now that slow and fast are the same, we need a pointer at the start of cycle
        # let slow be this pointer, and leave fast where it was on the cycle
        # let fast and slow progress at same speed, eventually theye will collide, and
        # you have your answer
        slow = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                return fast
        
