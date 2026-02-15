class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nei = defaultdict(list)
        wordList.append(beginWord)
        visited = set()

        for word in wordList:
            for letter in range(len(word)):
                pattern = word[:letter] + "*" + word[letter + 1:]
                nei[pattern].append(word)
        
        q = deque()
        q.append(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for letter in range(len(word)):
                    pattern = word[:letter] + "*" + word[letter + 1:]
                    for n in nei[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            res += 1
        return 0