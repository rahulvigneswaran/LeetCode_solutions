class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        # Counter alternative
        counts = Counter(nums)
        # for i in nums:
        #     counts[i] = 1 + counts.get(i, 0)
        
        freq = [[] for _ in range(len(nums)+1)]

        for v, c in counts.items():
            freq[c].append(v)
        
        out = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                out.append(j)
                if len(out) == k:
                    return out