class Trie:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word: str) -> None:
        curr = self
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Trie()
            curr = curr.children[letter]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        
        def dfs(node):
            if node.isWord:
                return True
            
            for nei in node.children.values():
                if dfs(nei):
                    return True
            return False

        return dfs(curr)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)