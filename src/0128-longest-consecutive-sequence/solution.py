class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.size = {}  # This keeps track of the size of each connected component

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                self.size[rootX] += self.size[rootY]

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.size[x] = 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Technically you can solve this using UFDS (Union Find). A sequence of numbers is just a set
        WE need to find the start of the sequence. If Im "0", Im automatically the start.
        If Im "100", see if theres a "99", if not Im the starting number so I will move on.
        We can do a while loop to find the next number.
        """
        res, num_set = 0, set(nums)
        for n in nums:
            if (n - 1) in num_set:
                # means we are not the start of the sequence and we can ignore
                continue
            else:
                current_length = 0
                while (n + current_length) in num_set:
                    current_length += 1
                res = max(current_length, res)
        return res

    def longestConsecutiveUnionFindDataStructure(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uf = UnionFind()
        for num in nums:
            uf.add(num)

        for num in nums:
            if num + 1 in uf.parent:
                uf.union(num, num + 1)

        # Find the maximum size of the connected components
        return max(uf.size.values())

