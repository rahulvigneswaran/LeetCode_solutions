class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])
        
        while minHeap:
            t, R, C = heapq.heappop(minHeap)
            if R == ROWS-1 and C == COLS-1:
                return t
            for dr, dc in dirs:
                new_R, new_C = R+dr, C+dc

                if ((new_R, new_C) not in visited and
                    (0 <= new_R < ROWS) and 
                    (0 <= new_C < COLS)):
                    visited.add((new_R, new_C))
                    heapq.heappush(minHeap, (max(t, grid[new_R][new_C]), new_R, new_C))
            

