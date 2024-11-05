import pytest
from leetcode.libs.binary_tree import TreeNode


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
            val=8
        )
    )

def test_has_path_sum(binary_tree: TreeNode):
    ...