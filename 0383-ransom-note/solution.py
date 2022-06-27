class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        words = set(ransomNote) 
        for i in words: 
            if magazine.count(i) < ransomNote.count(i): 
                return False 
        return True 
