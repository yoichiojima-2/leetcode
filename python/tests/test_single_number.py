from leetcode.single_number import Solution


def test_single_number():
    solution = Solution()
    assert solution.singleNumber([2, 2, 1]) == 1
    assert solution.singleNumber([4, 1, 2, 1, 2]) == 4
    assert solution.singleNumber([1]) == 1
