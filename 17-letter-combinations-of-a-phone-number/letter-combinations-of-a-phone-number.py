class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # have a mapping
        # simply just do a dfs. pop when coming out. better to using wording node, child
        # naive - backtracking
        # time : O(4^N)
        mapping = {
                    2: "abc",
                    3: "def",
                    4: "ghi",
                    5: "jkl",
                    6: "mno",
                    7: "pqrs",
                    8: "tuv",
                    9: "wxyz"
                }
        
        res = []
        subset = []

        #dfs
        def helper(node):
            if node >= len(digits):
                res.append("".join(subset))
                return
            
            for child in mapping[int(digits[node])]:
                subset.append(child)
                helper(node+1)
                subset.pop()
        
        helper(0)

        return res
