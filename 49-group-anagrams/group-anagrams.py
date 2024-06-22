class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        l = 0
        while l < len(strs):
            onehot = [0]*26
            for st in list(strs[l]):
                onehot[ord(st)-ord("a")] += 1  
            hashmap[tuple(onehot)].append(strs[l])
            l+=1
        
        return hashmap.values()
