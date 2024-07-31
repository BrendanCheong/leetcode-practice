class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Same idea as Subset II, we cannot have duplicates, so we must move the pointer
        when choosing the next number to the number where we have not encountered
        """
        # sort first so we will know if theres duplicate numbers in front of pointer
        candidates.sort()
        res = []

        def backtrackDFS(i: int, combo: List[int], total: int) -> None:
            # 1. Base case, we have hit the total
            if total == target:
                res.append(combo.copy())
                return
            
            # 2. Another case, where the node we are on is out of bounds of the candidates
            # or goes over the total, then don't include that node in the decision tree
            if i >= len(candidates) or total > target:
                return
            
            # 3. Left sub-tree, choose to add the candidate
            combo.append(candidates[i])
            backtrackDFS(i + 1, combo, total + candidates[i])
            
            # 4. Right sub-tree. choose to not add candidate, move pointer
            # until we find a number that we have not seen before
            # remember to pop so we remove the number we have seen before
            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            # i + 1, since we moved the pointer to the number before the non-duplicate number
            backtrackDFS(i + 1, combo, total)
        backtrackDFS(0, [], 0)
        return res
