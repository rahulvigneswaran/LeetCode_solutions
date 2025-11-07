class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        # dfs
        def helper(ind, total):
            if total == target:
                res.append(subset.copy())
                return
            
            if ind >= len(candidates) or total > target:
                return
            
            num = candidates[ind]
            subset.append(num)
            helper(ind + 1, total + num)
            subset.pop()

            while ind + 1 < len(candidates) and candidates[ind] == candidates[ind+1]:
                ind+=1
            
            helper(ind + 1, total)
        
        helper(0, 0)

        return res