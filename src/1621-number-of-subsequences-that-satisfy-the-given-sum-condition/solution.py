class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        # since its sorted, we can easily find min and max and use our pseudo binary search/2-pointer
        first, last, res = 0, len(nums) - 1, 0
        mod = pow(10, 9) + 7
        while first <= last:
            curr = nums[first] + nums[last]
            if curr <= target:
                # we found a subsequence! given an array of n length, there are 2^n subsequences
                res += pow(2, last - first, mod)
                res %= mod
                first += 1
            else:
                last -= 1
        return res


