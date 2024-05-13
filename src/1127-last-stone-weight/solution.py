from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        A typical max heap qns, anything with kth largest elements involves heaps

        We'll just add negative numbers when taking out of the heap and adding into the heap
        if we want to create max heaps

        Time: O(n * nlogk)
        Space: O(n)
        """
        max_heap = [-stone for stone in stones]
        heapify(max_heap)

        while len(max_heap) > 1:
            heaviest = heappop(max_heap)
            second_heaviest = heappop(max_heap)
            if heaviest != second_heaviest:
                new_stone = (-heaviest) - (-second_heaviest)
                heappush(max_heap, -new_stone)

        # edge case when both stones at the begining gets destroyed, we 
        # have to return something
        return -max_heap[0] if max_heap else 0
        
