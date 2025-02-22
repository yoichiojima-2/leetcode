import pytest

from leetcode.inorder_traversal import Solution
from leetcode.libs.binary_tree import TreeNode


@pytest.fixture
def binary_tree():
    return TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3)))


@pytest.fixture
def binary_tree_2():
    return TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            left=TreeNode(val=4),
            right=TreeNode(val=5, left=TreeNode(val=6), right=TreeNode(val=7)),
        ),
        right=TreeNode(val=3, right=TreeNode(val=8, left=TreeNode(val=9))),
    )


@pytest.fixture
def binary_tree_3() -> TreeNode:
    return TreeNode(val=1)


@pytest.fixture
def empty_binary_tree() -> None:
    return None


def test_inorder_traversal(
    binary_tree: TreeNode,
    binary_tree_2: TreeNode,
    binary_tree_3: TreeNode,
    empty_binary_tree: None,
):
    res_1 = Solution().inorderTraversal(binary_tree)
    assert res_1 == [1, 3, 2]

    res_2 = Solution().inorderTraversal(binary_tree_2)
    assert res_2 == [4, 2, 6, 5, 7, 1, 3, 9, 8]

    res_3 = Solution().inorderTraversal(binary_tree_3)
    assert res_3 == [1]

    res_4 = Solution().inorderTraversal(empty_binary_tree)
    assert res_4 == []
