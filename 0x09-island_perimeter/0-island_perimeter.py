#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid
    :param grid:
    :return:
    """
    perim = 0
    for row in grid + list(map(list, zip(*grid))):
        for i1, i2 in zip([0] + row, row + [0]):
            perim += int(i1 != i2)
    return perim
