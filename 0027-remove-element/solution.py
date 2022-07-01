class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j, ele in enumerate(nums):
            if (ele != val):
                nums[i] = nums[j]
                i += 1
                print(nums)
        return i
        
