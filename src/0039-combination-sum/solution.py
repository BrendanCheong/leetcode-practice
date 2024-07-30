class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, curr: List[int], total: int):
            # when we reached the end of the tree, the leaf nodes
            # we stop when we reached the target
            if total == target:
                # we will reuse this later, so create a copy of it
                # so we don't override it
                res.append(curr.copy())
                return
            
            # we can't find any more combo when we can no longer add anymore items to the combo
            # or when our total exceeds the target
            if i >= len(candidates) or total > target:
                return

            # left subtree, add to the combo and stay at that candidate
            # add to the total as well
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])

            # right subtree, don't add to the combo at all, stay as it is
            # so we pop from the combo so the combo stays as it is
            # and we move on to the next candidate
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
