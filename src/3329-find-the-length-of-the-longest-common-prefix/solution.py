class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number_str: str):
        node = self.root
        for char in number_str:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_number = True

    def longest_common_prefix(self, number_str: str) -> int:
        node = self.root
        length = 0
        for char in number_str:
            if char in node.children:
                node = node.children[char]
                length += 1
            else:
                break
        return length

class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(str(num))
        
        max_length = 0
        for num in arr2:
            max_length = max(max_length, trie.longest_common_prefix(str(num)))
        
        return max_length


