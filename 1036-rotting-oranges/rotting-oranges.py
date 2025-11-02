class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()
        fresh = [0]

        def helper(r, c):
            if (not(0 <= r < ROWS) or not(0 <= c < COLS) or
                grid[r][c] == 0 or (r, c) in visited):
                return 

            fresh[0] -= 1
            q.append([r, c])
            visited.add((r, c))
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh[0] += 1  
        
        time = 0
        while q and fresh[0] > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                helper(r+1, c)
                helper(r-1, c)
                helper(r, c+1)
                helper(r, c-1)  
            time += 1

        return time if fresh[0] == 0 else -1


        