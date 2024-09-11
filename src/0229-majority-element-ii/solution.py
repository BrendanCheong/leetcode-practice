class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        You can do Boyer Moore vote algorithm again!
        there is at most 2 majority elements
        not 3 or 4, 2 only. If there was 3, then each number would appear 1/3 times at most
        so 1/3 * 3 = n. But we want numbers appearing more than n/3. So max is 2

        **So given n/k is considered majority, there are k-1 majority elements
        Time: O(N)
        Space: O(1)
        """
        K = 3 # in this case k is 3
        candidate1, candidate2 = None, None
        vote1, vote2 = 0, 0
        
        # 1. Use Boyer moore algo on the array of nums, with 2 majority elements
        for ele in nums:
            # Need to check candidate first
            if candidate1 == ele:
                vote1 += 1
            elif candidate2 == ele:
                vote2 += 1
            # Then reset the vote last, so we dont reset unnecessarily
            elif vote1 == 0:
                candidate1 = ele
                vote1 = 1
            elif vote2 == 0:
                candidate2 = ele
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1
        
        # 2. Verify the candidates
        n = len(nums)
        candidate1_occurence, candidate2_occurence = 0, 0
        for num in nums:
            if num == candidate1:
                candidate1_occurence += 1
            elif num == candidate2:
                candidate2_occurence += 1
        
        # 3. Check if candidates appear more than ⌊n/3⌋ times
        res = []
        if candidate1_occurence > (n // K):
            res.append(candidate1)
        if candidate2_occurence > (n // K):
            res.append(candidate2)
        return res

