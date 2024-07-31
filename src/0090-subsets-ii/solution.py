class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Not a DP qns since we have to build the decision tree.
        The decision tree is such that we cannot have duplicated numbers in the subset
        we can do this by first sorting, and moving the pointer index to a number
        that we have not seen before

        Time: O(n 2 ^ n)
        Space: O(2 ^ n)
        """
        # sort so we don't run into duplicates as we move the index pointer forward
        nums.sort()
        res = []

        def dfs(i: int, subset: List[int]) -> None:
            # 1. Base case, is when we reached the leaf nodes, the end of the
            # decision tree
            if i == len(nums):
                res.append(subset.copy())
                return

            # 2. Left sub-tree, where we include nums[i], then move the index pointer
            # to the next number to add 
            subset.append(nums[i])
            dfs(i + 1, subset)
            # we must pop to remove the previous nums[i] for the next subtree
            subset.pop()

            # 3. Right sub-tree, we don't include nums[i]
            # we need to move the index to a number that we don't already have
            # using a while loop
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                # i + 1 must be in-bounds, as we will dfs(i + 1) later
                # if we get [1,2,2,3], we have 2 of the same number, so we move the pointer to the last duplicated number which is 2, so next dfs we start at number 3
                i += 1
            dfs(i + 1, subset)
        dfs(0, [])
        return res

