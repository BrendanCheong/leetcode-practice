from heapq import heappop, heappush, heapify

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Typical heap qns. We have to rebalance the heap initially or when adding. In this case
        we rebalance when initialised but you could also rebalance to kth element in the 'add' function

        Time: O(n * k (log n))
        Space: O(n)
        """
        self.min_heap = nums
        self.k = k
        heapify(self.min_heap)

        # given k, remove elements from min heap until we reach
        # the desired k elements. The top of heap will be kth largest element
        # Makes sense as we are sort of counting backwards from a sorted list.
        # since its a min heap. If it was a max heap its len(nums) - k
        while k < len(self.min_heap):
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
