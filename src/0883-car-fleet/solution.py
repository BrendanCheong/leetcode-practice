class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        The thing to take note of is time which is
        time = distance / speed
        distance in this case is distance between car and destination. We want to sort by position first then by speed
        So we start with the cars closest to the end point

        Cars who's time are overlapping can be grouped together, we can group cars 2 at a time.
        So if the current car's time is less than or equal to the previous car time, we can group them together
        Thats why we only check the stack if theres 2 cars in it. 
        The non stack solution is similar, we are checking the most recently calculated time.

        Time: O(n log n) for sorting
        Space: O(n)
        """
        cars = [(p, s) for p, s in sorted(zip(position, speed), reverse=True)]
        stack = []
        for p, s in cars:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
    def carFleetNonStackSolution(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in sorted(zip(position, speed), reverse=True)]
        remaining_time = -sys.maxsize
        groups = 0
        for p, s in cars:
            t = (target - p) / s
            if remaining_time < t:
                # Basically means that fast cars near to the destination get grouped together
                # so let say car A is reaching in 3 second while car B is reaching in 1, then A and B
                # get grouped together, especially if they are close to the end of the destination
                remaining_time = t
                groups += 1
        return groups

        
        
