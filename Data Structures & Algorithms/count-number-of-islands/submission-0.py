class Solution:
    def dfs(self, row, col, grid, visited):
        i = len(grid)
        j = len(grid[0])

        visited.add((row, col))

        directions = {(1,0), (-1, 0), (0, 1), (0, -1)}

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if 0 <= nr < i and 0 <= nc < j and grid[nr][nc] == "1" and (nr, nc) not in visited:
                self.dfs(nr, nc, grid, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        cnt = 0

        i = len(grid)
        j = len(grid[0])

        for row in range(i):
            for col in range(j):
                if grid[row][col] == "1" and (row, col) not in visited:
                    self.dfs(row, col, grid, visited)
                    cnt += 1

    
        return cnt