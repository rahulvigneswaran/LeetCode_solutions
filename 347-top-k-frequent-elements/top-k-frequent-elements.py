class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        keys, values = list(count_dict.keys()), list(count_dict.values())
        combined = [(k,v) for k, v in zip(keys, values)]        
        combined.sort(key=second, reverse=True)
        return [tup[0] for tup in combined[:k]]

def second(a):
    return a[-1]