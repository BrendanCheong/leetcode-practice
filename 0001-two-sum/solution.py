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
        
        If not in there, we can form the pair in the HashTable using {leftover: index}
        We use a HashTable for fast querying of O(1) time, we take O(n) time to loop through 
        the whole HashTable
        """
        dct = dict()
        for i, ele in enumerate(nums):
            leftover = target - ele
            if (leftover in dct): # if leftover is present
                return [dct[leftover], i]
            dct[ele] = i # add the index to the hashmap
        return [0, 0]
        
