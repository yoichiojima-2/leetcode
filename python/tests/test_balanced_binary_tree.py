import pytest

from leetcode.balanced_binary_tree import Solution, TreeNode


@pytest.fixture
def balanced_binary_tree() -> TreeNode:
    # fmt: off
    return TreeNode(
        val=3,
        left=TreeNode(val=9),
        right=TreeNode(
            val=20,
            left=TreeNode(val=15),
            right=TreeNode(val=7)
        ),
    )
    # fmt: on


@pytest.fixture
def balanced_binary_tree_2() -> TreeNode:
    return TreeNode(
        val=1,
    )


@pytest.fixture
def balanced_binary_tree_3() -> TreeNode:
    return TreeNode(val=1, left=TreeNode(val=2))


@pytest.fixture
def unbalanced_binary_tree() -> TreeNode:
    # fmt: off
    return TreeNode(
        val=1,
        right=TreeNode(
            val=2,
            right=TreeNode(
                val=3,
                right=TreeNode(val=4)
            )
        )
    )
    # fmt: on


@pytest.fixture
def unbalanced_binary_tree_2() -> TreeNode:
    return TreeNode(
        val=1,
        left=TreeNode(val=2, left=TreeNode(val=3, left=TreeNode(val=4))),
        right=TreeNode(val=2, right=TreeNode(val=3, right=TreeNode(val=4))),
    )


@pytest.fixture
def unbalanced_binary_tree_3() -> TreeNode:
    return TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            left=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=4)),
            right=TreeNode(val=3),
        ),
        right=TreeNode(val=2),
    )


@pytest.fixture
def empty_binary_tree() -> None:
    return None


def test_solution(
    balanced_binary_tree: TreeNode,
    balanced_binary_tree_2: TreeNode,
    balanced_binary_tree_3: TreeNode,
    unbalanced_binary_tree: TreeNode,
    unbalanced_binary_tree_2: TreeNode,
    unbalanced_binary_tree_3: TreeNode,
    empty_binary_tree: TreeNode,
):
    assert Solution().isBalanced(balanced_binary_tree)
    assert Solution().isBalanced(balanced_binary_tree_2)
    assert Solution().isBalanced(balanced_binary_tree_3)
    assert not Solution().isBalanced(unbalanced_binary_tree)
    assert not Solution().isBalanced(unbalanced_binary_tree_2)
    assert not Solution().isBalanced(unbalanced_binary_tree_3)
    assert Solution().isBalanced(empty_binary_tree)


def test_get_depth(
    balanced_binary_tree: TreeNode,
    balanced_binary_tree_2: TreeNode,
    balanced_binary_tree_3: TreeNode,
    unbalanced_binary_tree: TreeNode,
    unbalanced_binary_tree_2: TreeNode,
    unbalanced_binary_tree_3: TreeNode,
    empty_binary_tree: TreeNode,
):
    assert Solution().getDepth(balanced_binary_tree) == 3
    assert Solution().getDepth(balanced_binary_tree_2) == 1
    assert Solution().getDepth(balanced_binary_tree_3) == 2
    assert Solution().getDepth(unbalanced_binary_tree) == -1
    assert Solution().getDepth(unbalanced_binary_tree_2) == -1
    assert Solution().getDepth(unbalanced_binary_tree_3) == -1
    assert Solution().getDepth(empty_binary_tree) == 0
