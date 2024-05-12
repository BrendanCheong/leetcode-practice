from heapq import heappush, heappop

class MedianFinder:
    """
    The fundamental idea is to keep half of the data (the smaller numbers) in one structure
    and the other half (the larger numbers) in another structure. 
    By doing this, you can easily access the middle values, which could be the median!

    To manage a data stream for median calculations, use two heaps:
    1. Initialization:
    - small (max heap): stores the smaller half of numbers.
    - large (min heap): stores the larger half.

    2. Adding a Number:
    - Add to large if the number is greater than large's smallest number.
    - Otherwise, add the negated number to small.

    3. Balancing Heaps:
    - If small exceeds large by more than one, move the largest from small to large.
    - If large exceeds small by more than one, move the smallest from large to small (negated).

    4. Finding the Median:
    - If heaps are equal in size: median is the average of small's maximum and large's minimum.
    - If not equal: median is the larger heap's top element.

    Time: O(log n)
    Space: O(n)
    """

    def __init__(self):
        self.max_heap = [] # stores small numbers
        self.min_heap = [] # stores big numbers
        

    def addNum(self, num: int) -> None:
        # A number is big if its bigger than the smallest number in my min heap
        # My min heap contains the smallest biggest number we have
        if self.min_heap and self.min_heap[0] < num:
            heappush(self.min_heap, num)
        else:
            # By default, heapq is a min heap
            heappush(self.max_heap, -num)

        # We need to balance the 2 heaps, we want the min heap to store big numbers
        # and we want the max heap to store small numbers
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heappop(self.min_heap) # this is the smallest big num
            heappush(self.max_heap, -val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heappop(self.max_heap)
            heappush(self.min_heap, val)
        
    def findMedian(self) -> float:
        # if one heap is bigger than the other, we take the top of that value!
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # if both same length, we take both ends and calculate!
        big, small = self.min_heap[0], -self.max_heap[0]
        return (big + small) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
