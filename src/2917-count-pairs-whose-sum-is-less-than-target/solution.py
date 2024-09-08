class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Step 1: Find the min and max values in nums to limit our frequency array range
        min_val = min(nums)
        max_val = max(nums)
        
        # Step 2: Create a frequency array to count occurrences of each number
        freq = [0] * (max_val - min_val + 1)

        # Fill in the frequency array
        for num in nums:
            freq[num - min_val] += 1
        
        # Step 3: Create a prefix sum array to count how many numbers are <= each index
        prefix_sum = [0] * (max_val - min_val + 1)
        prefix_sum[0] = freq[0]
        
        for i in range(1, len(freq)):
            prefix_sum[i] = prefix_sum[i - 1] + freq[i]

        # Step 4: Count valid pairs
        count = 0
        for num in nums:
            limit = target - num - 1
            
            # Ensure limit is within the bounds of our frequency/prefix_sum array
            if limit >= min_val:
                # Calculate the index in the prefix sum array
                index = min(limit - min_val, max_val - min_val)
                count += prefix_sum[index]
            
            # Subtract the current element itself if it was counted (i.e., i == j)
            if num * 2 < target:
                count -= 1
        
        # Since we counted each pair twice, divide the count by 2
        return count // 2
