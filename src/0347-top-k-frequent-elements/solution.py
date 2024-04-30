from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        You can use the bucket sort algo to solve this qns in O(n) time.
        Modified bucket sort, instead of index = element and value = occurence,
        we do index = occurence, value = element
        Time complexity is O(n)
        Space complexity is O(n)
        """

        # default value is 0
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        # The max array size is k + 1, as we cannot have 0 array size since there
        # will always be an occurence, so we do + 1
        # Ex: if the array is size 6, could we have 100 max occurences of lets say "1"?
        # of course not, then we would need an array size >= 100 
        buckets = [[] for n in range(len(nums) + 1)]

        # populate our bucket, we can have multiple numbers having the same occurence
        # like number 10, can occur once, so can number 1
        # our bucket looks like this -> [[], [10, 1], [2]]
        for num, freq in hashmap.items():
            buckets[freq].append(num)

        res = []
        # iterate backwards, its faster this way, cuz we want the highest occuring number (k)
        # not the lowest occuring number
        for i in range(len(buckets) - 1, 0, -1):
            bucket = buckets[i]
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        """
        You can also use a heap to solve this qns.
        Time complexity is O(nlogk)
        Space complexity is O(n)
        """
        # populate the dictionary with all occurences
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1

        # create a heap
        heap = []
        for n, v in hashmap.items():
            heapq.heappush(heap, (v, n))
            # If the heap is larger than k, we pop the smallest element 
            # because we want to keep the largest k elements
            if len(heap) > k:
                heapq.heappop(heap)

        return [n for v, n in heap]
