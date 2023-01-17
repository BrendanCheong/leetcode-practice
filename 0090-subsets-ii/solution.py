class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n log n + n2^n)
        Space: O(n 2^n)
        """
        res = []
        subset = []
        # algo only works assuming that the numbers given are in ascending order, as we move the pointer according to duplicates
        nums.sort()
        def dfs(i: int):

            # base case is when we iterate until we reach the end of the list
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # we dont want the right subtree so we pop
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # move the pointer until we dont reach any duplicates
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res
