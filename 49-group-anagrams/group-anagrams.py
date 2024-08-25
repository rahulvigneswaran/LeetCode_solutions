class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        mapping = defaultdict(list)
        for word in strs:
            index = [0]*26
            word_map = Counter(word)
            for key in word_map.keys():
                index[ord(key) - ord("a")]+=word_map[key]
            mapping[str(index)].append(word)
        return list(mapping.values())
