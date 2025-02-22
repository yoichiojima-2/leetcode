class Solution:
    def generate_next_row(self, bottom) -> list[int]:
        first = bottom[0]
        last = bottom[-1]
        middle = []
        for i in range(len(bottom) - 1):
            middle.append(bottom[i] + bottom[i + 1])
        return [first, *middle, last]

    def generate(self, num_rows: int) -> list[list[int]]:
        res = [[1]]
        for i in range(num_rows - 1):
            res.append(self.generate_next_row(res[-1]))
        return res

    def getRow(self, rowIndex: int) -> list[int]:
        triangle = self.generate(rowIndex + 1)
        return triangle[rowIndex]
