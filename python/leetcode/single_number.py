from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counter = Counter(nums)
        return [n for n, count in counter.items() if count == 1][0]
