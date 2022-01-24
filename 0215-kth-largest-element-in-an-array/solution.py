class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k  = len(nums) - k # to find k largest, for k smallest its k - 1
        def quickSelect(l: int, r: int) -> int:
            pivot = nums[r]
            p = l
            for  i in range(l, r):
                if (nums[i] <= pivot): # iterate through whole array
                    nums[p], nums[i] = nums[i], nums[p] # swap the partitioned value IF "r" is the biggest, to move on to next biggest
                    p += 1 # increment the p pointer so we get the final place where we can partition
            nums[p], nums[r] = nums[r] , nums[p] # last swap to get new pivot
            if (p > k):
                return quickSelect(l, p - 1) # look at the left portion of the array
            elif (p < k):
                return quickSelect(p + 1, r); # look at the right portion of the array
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1) # pivot selected is just the last value
            
                    
                    
                    
        
