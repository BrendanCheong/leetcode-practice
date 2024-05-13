from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        You can use min heap for this solution, but its not the most
        memory efficient. A better method would be to use partition and quick select,
        components of quicksort!

        Partition and Heaps go hand in hand for kth elements!

        Time: O(n k log n)
        Space: O(n)
        """
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        return nums[0]
        
