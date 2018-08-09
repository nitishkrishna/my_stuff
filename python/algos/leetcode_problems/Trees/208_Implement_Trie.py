class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.isEnd = False
        self.children = {}
    
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("#")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur_node = self.root
        idx_to_save_from = None
        for idx, char in enumerate(word):
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                idx_to_save_from = idx
                break
        
        if idx_to_save_from is not None:
            for char in word[idx_to_save_from:]:
                cur_node.children[char] = TrieNode(char)
                cur_node = cur_node.children[char]
        
        cur_node.isEnd = True
            
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur_node = self.root
        for char in word:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
            
        if cur_node.isEnd:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur_node = self.root
        for char in prefix:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# 39.70%
