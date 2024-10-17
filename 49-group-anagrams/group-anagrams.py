class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        res = defaultdict(list)

        for word in strs:
            template = [0]*26
            for letter in word:
                ind = ord(letter) - ord("a")
                template[ind] += 1
            res[tuple(template)].append(word)
        return list(res.values())
# Use the frequency [0]*26 of each word as key in a dict.
# Optimized solution >> Time : O(n*m). Space : O(n*m). n is words. m is len of words.