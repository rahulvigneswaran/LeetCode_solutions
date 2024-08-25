class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        counts = [(counts[key], key) for key in counts.keys()]
        counts = sorted(counts, key=temp)[::-1]
        counts = counts[:k]
        return [i[-1] for i in counts]

def temp(a):
    return a[0]