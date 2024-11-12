import pytest
from leetcode.libs.binary_tree import TreeNode
from leetcode.path_sum import Solution


@pytest.fixture
def binary_tree() -> TreeNode | None:
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

def test_has_path_sum(binary_tree: TreeNode):
    assert Solution().hasPathSum(binary_tree, 22)