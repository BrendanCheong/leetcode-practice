class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        A tricky one, the trick is to iterate backwards! and then keep track of the MAX element           you have encountered. If you iterate forwards you will find that:

        you will need to do O(n^2) time to keep looking forwards to find the max element
        
        The Algo: Going backwards, the first max ele is -1, replace the end ele with the max
        then update the max ele, keep going until we reached the end of the array
        """
        MAX = -1
        for i, ele in reversed(list(enumerate(arr))):
            arr[i] = MAX
            # update MAX
            MAX = max(ele, MAX)
        return arr
            
