from collections import defaultdict
import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Naive solution would be to create a dictionary for each word
        then O(n^2) loop, for each word find the matching dictionary with
        the same value
       
        Another idea is to sort the words, but its gonna take N log N for M times which is M = length of array
        
        The trick is that in order to find matching words in O(1) time, we have to use tuples!!! and HashMaps. So each word has its own tuple (which is the character count) and we can match the word(s) to its tuple(s)
        
        This is O(m * n) time, m number of words, n length of each word
        space is O(n)
        """
        res = defaultdict(list) # dct of character count arrays
        
        for i, word in enumerate(strs):
            char_arr = [0] * 26 # create blank char arr for each word
            for j in word:
                char_arr[ord(j) - ord('a')] += 1
            # now that we have our char arr we can add it to our dict
            # have to use tuple to make it unique
            # add the corresponding word to char_arr
            res[tuple(char_arr)].append(word)
        # only return the values with the array
        return res.values()
            
                
        
