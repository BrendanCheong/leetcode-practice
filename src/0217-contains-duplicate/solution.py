class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        The most obvious solution is a hashset to keep track of all the numbers you have seen
        If I have seen a number in my hashset/memory, then I have found the answer.

        A low Big-O space would be to sort and use bit manipulation, but thats
        O(n log n) time and O(1) space

        Time: O(n)
        Space: O(n)
        """
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
