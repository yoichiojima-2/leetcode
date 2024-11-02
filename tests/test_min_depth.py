import pytest

from leetcode.libs.binary_tree import TreeNode
from leetcode.min_depth import Solution


@pytest.fixture
def binary_tree_1() -> TreeNode:
    return TreeNode(
        val=3,
        left=TreeNode(val=9),
        right=TreeNode(
            val=21,
            left=TreeNode(val=15),
            right=TreeNode(val=1)
        )
    )


@pytest.fixture
def binary_tree_2() -> TreeNode:
    return TreeNode(
        val=2,
        right=TreeNode(
            val=3,
            right=TreeNode(
                val=4,
                right=TreeNode(
                    val=5,
                    right=TreeNode(val = 6)
                )
            )
        )
    )


def test_min_depth(binary_tree_1, binary_tree_2):
    assert Solution().minDepth(binary_tree_1) == 2
    assert Solution().minDepth(binary_tree_2) == 5
