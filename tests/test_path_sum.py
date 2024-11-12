import pytest
from leetcode.libs.binary_tree import TreeNode
from leetcode.path_sum import Solution


@pytest.fixture
def binary_tree() -> TreeNode:
    return TreeNode(
        val=5,
        left=TreeNode(
            val=4,
            left=TreeNode(
                val=11,
                left=TreeNode(val=7),
                right=TreeNode(val=2)
            ),
        ),
        right=TreeNode(
            val=8,
            left=TreeNode(val=13),
            right=TreeNode(
                val=4,
                right=TreeNode(val=1)
            )
        )
    )


@pytest.fixture
def binary_tree_2() -> TreeNode:
    return TreeNode(
        val=1,
        left=TreeNode(val=2)
    )



def test_has_path_sum(binary_tree: TreeNode):
    assert Solution().hasPathSum(binary_tree, 22)


def test_has_path_sum_1():
    assert not Solution().hasPathSum(None, 0)


def test_has_path_sum_2(binary_tree_2):
    assert not Solution().hasPathSum(binary_tree_2, 1)
