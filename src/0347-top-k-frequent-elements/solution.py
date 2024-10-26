from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i, ele in enumerate(nums):
            hashmap[ele] += 1
        # since we are sorting based on occurence, we can use buckets based on length of nums
        # if we were sorting based on min num and max num, then its a bit different
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, occurence in hashmap.items():
            buckets[occurence].append(num)

        # Now we can iterate backwards, with highest occurence at the end of the array
        res = list()
        for i in range(len(buckets) - 1, -1, -1):
            if k == 0:
                return res
            if buckets[i]:
                res += buckets[i]
                # there could be more than one element in the bucket
                k -= len(buckets[i])

        return res
