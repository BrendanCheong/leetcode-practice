class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        WE create a backtracking graph

        The left part of the subtree includes the number in the array
        the right part of the subtree does not
        recursively form this tree
                /     \
              [1]     []
        add 2 / \     / \
         [1, 2]  [1] [2] []
        """
        res = []
        subset = []
        def dfs(index: int) -> None:
            # base condition, if index increases out of bounds, we have found the answer
            if index >= len(nums):
                res.append(subset[:]) # add a copy of the subset
                return
            
            # left subtree adds elements from the array
            subset.append(nums[index])
            dfs(index + 1)

            # right subtree does not add elements, since we added before we just pop it out
            subset.pop()
            dfs(index + 1)
        dfs(0)
        return res

