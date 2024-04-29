from collections import defaultdict
from typing import *
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        You can use the bucket sort algo to solve this qns in O(n) time.
        Modified bucket sort, instead of index = element and value = occurence,
        we do index = occurence, value = element
        """
        # populate the dictionary with all occurences
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1

        
        # create a frequency bucket array. Each index of this array is the possible highest occurence
        # of the nums array. Ie: the max occurence = max_occur + 1
        # why use max + 1 and not just max? cos we don't have 0 occurences, so the index is usually 0, 1, 2...
        # we want to + 1 so we get to the end

        freq = [[] for n in range(len(nums) + 1)]

        # populate the freq array
        for n, v in hashmap.items():
            freq[v].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        
        
