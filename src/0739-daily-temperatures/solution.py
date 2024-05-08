class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        # Result array initialized with 0's as some days might not have a warmer day
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            # Check if the current day is warmer than the day indexed at the top of the stack
            while stack and temperatures[stack[-1]] < temp:
                # Pop the index and calculate the number of days until this warmer temperature
                index = stack.pop()
                res[index] = i - index
            # Push the current index onto the stack
            stack.append(i)
        
        return res
