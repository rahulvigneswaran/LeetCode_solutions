class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        #dfs
        def helper(ind, total, subset):
            if total == target:
                res.append(subset.copy())
                return 
            
            if total > target or ind >= len(candidates):
                return

            for i in range(ind, len(candidates)):
                
                if i > ind and candidates[i] == candidates[i-1]:
                    continue

                num = candidates[i]

                helper(i + 1, total + num, subset + [num])
        
        helper(0, 0, [])
        return res