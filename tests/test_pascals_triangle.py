from leetcode.pascals_triangle import Solution


def test_pascals_triangle():
    solution = Solution()
    assert solution.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
