class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize UFDS
        par = {num: num for num in nums}
        rank = {num: 1 for num in nums} # start of from 1, cuz means the group has 1 node

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2] # Add the sizes of the groups together
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        # Union consecutive elements
        for num in nums:
            if num - 1 in par:
                union(num, num - 1)
            if num + 1 in par:
                union(num, num + 1)

        # Find the largest set
        return max(rank.values())
