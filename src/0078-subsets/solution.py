class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        This requires a Decision-tree, where we can form all the decisions
        then iterate through every decision to create the subsets needed

        The decisions are:
        1. Include the number in the array
        2. Don't include the number in the array
        We go down this decision tree until we can add no more numbers to the subset

                / \ 
            [1]    []
            / \   /  \
        [1,2] [1][2]  []
        /    \
     [1,2,3] [1,2]
        and so on...
        We stop when we run out of numbers to add to the subset
        That means we are at the leaf nodes of the decision tree

        Time: O(2 ^ n), since we are going to build every decision possible
        """
        res = []
        subset = []
        def dfs(i: int) -> None:
            # base case, we cannot add anymore numbers to the subset
            if i >= len(nums):
                res.append(subset.copy())
                return

            # The left side of the tree adds numbers to the subset
            subset.append(nums[i])
            dfs(i + 1) # go through left subtree

            # The right side of the tree doesn't add numbers to the subset
            # in that case, we pop from the subset
            subset.pop()
            dfs(i + 1) # go through right subtree
         
        dfs(0)
        return res
