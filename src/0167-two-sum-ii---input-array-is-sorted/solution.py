class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        2 pointer solution in using the sorted list trick.
        Since we're guaranteed to have a solution, we can just have 2 pointers, one
        at each end, and we can move the pointers until we find a solution. In a sense
        this is a greedy algo, as theres always a solution.

        Simply move the left pointer forward to the right if we need a bigger current number
        Then move the right pointer backwards if we need a smaller current number
        Technically, both pointers will never cross each other as there's always a solution.

        Time: O(n)
        Space: O(1)
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            # If we have found the solution, return it
            # Okay so for some reason the qns wants us to +1 the pointers lol
            # I guess they have 0 indexing??? What is this Lua?
            if current == target:
                return [left + 1, right + 1]
            # If too big, we need to be smaller, right pointer is always at bigger numbers 
            # since its a sorted list
            elif current > target:
                right -= 1
            # If too small, go bigger, left pointer is always at the smallest number
            # since its a sorted list
            else:
                left += 1
