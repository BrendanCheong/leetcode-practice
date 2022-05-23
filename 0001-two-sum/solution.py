class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n), with O(1 + α) amortized HashTable operation
        Explanation: Each element has its leftover amount given the target
        like for example, given target 9, and element 2 will have leftover 7
        and element 7 will have leftover 2.
        
        When there is a pair of leftovers that are inside the array, we have an answer.
        We can store each {ele: leftover} and check to see if the leftover is in the HashTable
        to create this pair, for each element.
        """
        dct = dict()
        for i in range(0, len(nums)):
            leftover = target - nums[i]
            if (leftover in dct):
                return [dct[leftover], i]
            else:
                dct[nums[i]] = i
        return false
        
