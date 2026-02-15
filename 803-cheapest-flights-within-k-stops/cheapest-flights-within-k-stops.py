class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        res = [float("inf")]*n
        res[src] = 0
        resTemp = res.copy() 

        for _ in range(k+1):
            for i, j, w in flights:
                if res[i] + w < resTemp[j]:
                    resTemp[j] = res[i] + w
            res = resTemp.copy()
        
        return res[dst] if res[dst] != float("inf") else -1