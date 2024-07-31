class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        An easier way to think of permuations is to start from the back (or first number)
        Lets say we have 1,2,3, lets start with 3. From 3 we say we add no numbers to it.
        The from 3 we can add 2. So we can either add 2 from the back or front
        so its 2,3 or 3,2. Then lastly we have 1, we can add 1 from back, front, or middle
        so we have 1,2,3 or 3,2,1, 3,1,2 etc.. We stop when we have no numbers.

        Basically, we take the permuations of nums without the first num.
        So from 1,2,3, we get 2,3 or 3,2. Then insert the first number in every index
        """
        # 0. Edge case, if nums is empty
        if not len(nums):
            return [[]]
        
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
