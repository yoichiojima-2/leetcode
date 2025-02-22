example = [
    [1],
    # [1, 1],
    # [1, 2, 1],
    # [1, 3, 3, 1],
    # [1, 4, 6, 4, 1]
]




class Solution:
    def generate_next_row(self, bottom) -> list[int]:
        first = bottom[0]
        last = bottom[-1]
        middle = []
        for i in range(len(bottom) - 1):
            middle.append(bottom[i] + bottom[i + 1])
        return [first , *middle, last]


    def generate(self, num_rows: int) -> list[list[int]]:
        res = [[1]]
        for i in range(num_rows - 1):
            res.append(self.generate_next_row(res[-1]))
        return res
    