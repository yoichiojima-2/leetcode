# 2352. Equal Row and Column Pairs
# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements 
# in the same order (i.e., an equal array).


def solution(grid):
    for g in grid:
        print(g)

testcases = [
    [[3,2,1],
     [1,7,6],
     [2,7,7]],

    [[3,1,2,2],
     [1,4,4,5],
     [2,4,2,2],
     [2,4,2,2]]
]

results = []

for i in testcases:
    data = {}
    data["input"] = i
    data["output"] = solution(i)
    results.append(data)

print(results)