def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        # Base case: out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return

        grid[r][c] = '0'  # Mark current cell as visited (sink the land)

        # Explore all 4 directions
        dfs(r+1, c)  # down
        dfs(r-1, c)  # up
        dfs(r, c+1)  # right
        dfs(r, c-1)  # left

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)  # Sink the entire island
                count += 1  # Count this island

    return count
