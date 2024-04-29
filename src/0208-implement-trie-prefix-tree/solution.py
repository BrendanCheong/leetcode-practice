class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                # if not a neighbor, create the node
                node.children[char] = TrieNode()
            # carry on to next node
            # we use either the node thats there or the node we just created
            node = node.children[char]
        node.is_word = True # at the end of the word, the last node is marked

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.children:
                # if word exists, carry on to the next node
                node = node.children[char]
            else:
                # if not exists, return False
                return False
        # find out if the last node is marked as the end word
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        # prefix checker
        node = self.root
        for char in prefix:
            if char in node.children:
                # if prefix exists, carry on to the next node
                node = node.children[char]
            else:
                # if not exists, return False
                return False
        # if we reached the end, we found the prefix
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
