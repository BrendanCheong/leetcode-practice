class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Use a sliding window approach with two pointers, 
        first and second, tracking the start and end of the substring. 
        A dictionary char_index records each character's latest index. 
        If a repeat is detected, first moves past the last occurrence, 
        continuously updating the maximum substring length.

        A more memory efficient solution could use a 26 character array,
        similar to bucket sort array

        Time: O(n)
        Space: O(n)
        """
        first, second, res = 0, 0, 0
        char_index = dict() # character : index

        # less than length, we wont go out of bounds
        while second < len(s):
            if s[second] in char_index and char_index[s[second]] >= first:
                # bring the beginning of the window to
                # one position infront the second 
                first = char_index[s[second]] + 1

            # update the character with the new end of sliding window index
            char_index[s[second]] = second
            res = max(second - first + 1, res)
            second += 1


        return res
