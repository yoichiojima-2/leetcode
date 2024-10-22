import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from climb_stairs import Solution


def test_climb_stairs():
    assert Solution().climbStairs(0) == 1
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
