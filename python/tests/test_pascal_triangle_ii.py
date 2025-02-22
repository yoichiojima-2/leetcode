from leetcode.pascals_triangle_ii import Solution


def test_pascals_triangle_ii():
    solution = Solution()
    assert solution.getRow(0) == [1]
    assert solution.getRow(1) == [1, 1]
    assert solution.getRow(2) == [1, 2, 1]
    assert solution.getRow(3) == [1, 3, 3, 1]
    assert solution.getRow(4) == [1, 4, 6, 4, 1]
