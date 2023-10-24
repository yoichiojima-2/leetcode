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

testcases = [
    [[3,2,1],[1,7,6],[2,7,7]],
    [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
]

results = []
for i in testcases:
    res = Solution().equalPairs(i)
    results.append({"input": i, "output": res})

print(results)