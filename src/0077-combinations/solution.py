class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, subset = [], []
        def dfs(i: int):
            if len(subset) == k:
                res.append(subset.copy())
                return
            for i in range(i, n + 1):
                subset.append(i)

                # go down the subtree
                dfs(i + 1)

                # backtrack
                subset.pop()
        dfs(1)
        return res

                
