from leetcode.climb_stairs import Solution


def test_climb_stairs():
    assert Solution().climbStairs(0) == 1
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
