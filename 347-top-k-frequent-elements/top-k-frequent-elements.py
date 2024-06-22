class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        freq =[[] for i in range(len(nums)+1)]
        
        for key, val in count_dict.items():
            freq[val].append(key)
        
        topk = []
        for i in range(len(freq)-1, 0, -1):
            if len(freq[i])>0:
                for j in freq[i]:
                    topk.append(j)
                    if len(topk) == k:
                        return topk
        return topk