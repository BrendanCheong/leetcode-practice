class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i: int, total: int):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            subset.append(candidates[i])

            # decision 1: add the same number
            dfs(i, total + candidates[i])
            
            # decision 2: add the next number
            subset.pop()
            dfs(i + 1, total)
        dfs(0, 0)
        return res

