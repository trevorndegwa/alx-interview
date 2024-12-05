#!/usr/bin/python3
"""
Function to calculate the perimeter of an island in a grid
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the grid island
    Args:
        grid: 2D grid where 0 (water) & 1 (land)
    Returns:
        int: Perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with a full perimeter for current cell
                perimeter += 4

                # Check all 4 possible neighbours and reduce perimeter
                if i > 0 and grid[i - 1][j] == 1:  # Up
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Down
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Right
                    perimeter -= 1

    return perimeter 
