class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        # Counter alternative
        for i in nums:
            counts[i] = 1 + counts.get(i, 0)
        
        freq = [[] for _ in range(len(nums)+1)]

        for v, c in counts.items():
            freq[c].append(v)
        
        out = []
        for i in range(len(freq)-1, 0, -1):
            if k > 0:
                avail = len(freq[i])
                if avail > k:
                    out = out + freq[i][:k]
                else :
                    out = out + freq[i]
                k -= avail
            else:
                break
        return out