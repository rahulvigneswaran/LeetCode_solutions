class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastInd = {}
        for ind, ch in enumerate(s):
            lastInd[ch] = ind
        
        res = []
        size = end = 0
        for ind, ch in enumerate(s):
            size += 1
            end = max(end, lastInd[ch])

            if ind == end:
                res.append(size)
                size = 0
            
        return res