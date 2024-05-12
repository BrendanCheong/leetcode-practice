class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        The solution to this is a increasing monotonic stack, where as the stack adds elements,
        it must make sure all the elements in the stack are of increasing order, popping previous
        elements to do so.

        First intuition is to solve the problem greedily, finding all possible max areas and updating
        accordingly.


        Time: O(n)
        Space: O(n)
        """
        max_area = 0
        stack = [] # pair (index, height), we index it as index = pair[-2] and height = pair[-1]

        for curr_index, curr_height in enumerate(heights):
            start = curr_index

            # We must keep the stack in increasing monotonic order
            # when that happens we can find the max area of all prev values
            # As we only want to find areas when the prev's bar's height is bigger than what we have now
            while stack and curr_height < stack[-1][-1]:
                # now we must find max area, which is width * height
                # width being index we are at now - the prev's bar index
                index, height = stack.pop()
                width = curr_index - index
                max_area = max(max_area, width * height)

                # special trick here, we want calculate the area between lowest and prev's bar higher height
                # so we say that we start from the prev's bar index and use the current lower height
                start = index

            stack.append((start, curr_height))

        # After iteration we will have some leftover items in the stack we must account for their area
        # But we can guarantee that the stack is 100% monotonic increasing stack order
        # so its easy to calculate now
        for i, h in stack:
            # width is last index of list - the start of begining of stack
            width = len(heights) - i
            max_area = max(max_area, width * h)
        return max_area
