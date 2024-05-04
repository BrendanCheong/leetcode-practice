class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        This uses the Hashtable method, we basically keep track of every number's desired number
        So if target is t = 9, and current number is 2, the desired is 7
        keep this in a hashmap, like so Map[desired number] = current number's index
        Then for each number we check if the desired number is in there
        Return if it is. Note that there can be negative numbers in the array

        Time: O(n)
        Space: O(n)
        """
        mem = dict()
        for index, num in enumerate(nums):
            if num in mem:
                first, second = mem[num], index
                return [first, second]
            mem[target - num] = index
