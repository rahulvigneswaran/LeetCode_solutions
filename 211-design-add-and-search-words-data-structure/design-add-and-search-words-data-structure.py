class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str) -> None:
        curr = self
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = WordDictionary()
            curr = curr.children[letter]
        curr.isWord = True

    def search(self, word: str) -> bool: 
        def dfs(node, ind):
            if ind == len(word):
                return node.isWord
            
            letter = word[ind]
            if letter == ".":
                for child in node.children.values():
                    if dfs(child, ind+1):
                        return True
                return False
            
            if letter not in node.children:
                return False
            
            node = node.children[letter]
            return dfs(node, ind+1)
        
        return dfs(self, 0)
  # Same as trie. Do a dfs. If we encounter ".", then run DFS for all children          


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)