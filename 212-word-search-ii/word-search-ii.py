class TrieNode:
    def __init__(self,):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        curr = self
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        visited = set()
        root = TrieNode()
        for w in words:
            root.addWord(w)

        def dfs(R, C, node, word):
            if (R < 0 or C < 0
                or R == ROWS or C == COLS
                or (R,C) in visited
                or board[R][C] not in node.children):
                return
            
            visited.add((R,C))
            node = node.children[board[R][C]]
            word += board[R][C]
            if node.isWord:
                res.add(word)
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr, dc in directions:
                dfs(R+dr, C+dc, node, word)
            visited.remove((R,C))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)

# Brute Force solution >> Remove all the words whose starting letter doesnt exist in the board. Then do a dfs for each word. Time Complexity >> O(w*(mn)*4^mn). Each dfs take 4^mn. tThere are mn elements in the grid. Have to do for w words.

# Optimized solution >> Use a Trie. Do a dfs. At each step of the dfs, compare the correspoding path in the Trie. Instead of looping, we can just check for isWord tag in Trie Node. Time Complexity >> O((mn)*4^mn). Each dfs take 4^mn. There are mn elements in the grid. But we dont have to do it separately for each word.