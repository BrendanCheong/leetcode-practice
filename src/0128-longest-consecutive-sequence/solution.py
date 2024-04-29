class UF:
    def __init__(self, n: int) -> None:
        self.parent = {i: i for i in range(n)} # set
        self.size = {i: 1 for i in range(n)} # set
    
    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        # path compression
        if self.size[rootX] <= self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        # path compression
        else: 
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
    
    def find_max(self) -> int:
        # O(n) time to find max value by iterating through all the groups
        return max(self.size.values())

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        n = len(nums)
        
        # This UF only accepts numbers
        uf = UF(n)
        dic = dict()
        
        # populate the UF by union joining the groups
        for i, num in enumerate(nums):
            if num in dic:
                continue

            dic[num] = i

            if (num + 1 in dic):
                uf.union(i, dic[num + 1])

            if (num - 1 in dic):
                uf.union(i, dic[num - 1])
        
        return uf.find_max()
                
