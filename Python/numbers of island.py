import collections

def numIslands( grid: list[list[str]]) -> int:
    if not grid:
        return 0
    row_max, col_max = len(grid), len(grid[0])
    count = 0
    def bfs(r, c):
        que = collections.deque()
        que.append((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        grid[r][c] = "0"  # Mark as visited by setting to "0"
        while que:
            row, col = que.popleft()
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if (nr in range(row_max) and 
                    nc in range(col_max) and 
                    grid[nr][nc] == "1"):
                    grid[nr][nc] = "0"  # Mark as visited by setting to "0"
                    que.append((nr, nc))
    for r in range(row_max):
        for c in range(col_max):
            if grid[r][c] == "1":  # If land is found
                bfs(r, c)
                count += 1  # Increase the island count
    return count