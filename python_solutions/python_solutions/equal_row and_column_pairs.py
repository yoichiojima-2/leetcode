from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            for j in range(len(grid[0])):
                col = [r[j] for r in grid]
                rows_equals_columns = col == i
                if rows_equals_columns:
                    count += 1

        return count
