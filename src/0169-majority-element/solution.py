class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        *IMPORTANT: The Boyer Moore Algo
        algorithm works on the fact that if an element occurs more than N/2 times, 
        it means that the remaining elements other than this would definitely be less than N/2. 

        The key insight is that the majority element, if it exists, will always survive the pairing process 
        because it appears more than n/2 times. 
        All other elements can at most cancel out n/2 occurrences of the majority element, 
        leaving at least one occurrence to be picked as the final candidate.

        Basically, a vote for a candidate increase by 1, a non-vote decrease by 1
        we will never have 0 votes for the majority candidate
        
        Time: O(n)
        Spac: O(1)
        """
        candidate = -1
        votes = 0
        for i, ele in enumerate(nums):
            if votes == 0:
                candidate = ele
                votes = 1
            elif ele != candidate:
                votes -= 1
            elif ele == candidate:
                votes += 1
        return candidate 
